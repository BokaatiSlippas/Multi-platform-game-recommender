<?php
session_start();

	include("functions.php");

	if(isset($_POST["done"]))
	{
		// Check if the user still has available recommendation requests available for the day
		$request_id = 0;
		
		$user_id = $_SESSION['user_id'];

		// Connect to the users database
		$dbhost = "localhost";
		$dbuser = "root";
		$dbpass = "";
		$dbname = "users_db";

		$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

		$query = "SELECT daily_recommendations_num FROM users WHERE user_id='$user_id'";

		$result = mysqli_query($con, $query);

		$result_arr = mysqli_fetch_assoc($result);
		
		$daily_recommendations_num = array_values($result_arr)[0];

		if (intval($daily_recommendations_num) >= 1)
		{
			// User recommendation details posted
			$preferred_genre = $_POST["preferred_genre"];
			$slider_value = $_POST["slider_value"];

			// Connect to the games database
			$dbhost = "localhost";
			$dbuser = "root";
			$dbpass = "";
			$dbname = "games_db";

			$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

			// Check what type of recommendation wanted
			if($preferred_genre == "*")
			{
				$genre_id = -1;
			}
			else
			{
				$query = "SELECT id FROM genres WHERE name='$preferred_genre'";

				$result = mysqli_query($con, $query);

				$genre_id_arr = mysqli_fetch_assoc($result);

				if(is_null($genre_id_arr))
				{
					die("Genre does not exist. Go back and re-enter an existing genre.");
				}
				
				$genre_id = array_values($genre_id_arr)[0];
			}

			// Connect to the users database
			$dbhost = "localhost";
			$dbuser = "root";
			$dbpass = "";
			$dbname = "users_db";

			$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

			// Post request
			$query = "INSERT INTO sync_requests (user_id,request_id,request_timestamp,request_int,request_int2,complete,server_output) VALUES ('$user_id','$request_id',CURRENT_TIMESTAMP(),'$genre_id','$slider_value',0,NULL)";

			$result = mysqli_query($con, $query);

			// Decrement daily_recommendations_num
			$daily_recommendations_num = intval($daily_recommendations_num) - 1;

			$query = "UPDATE users SET daily_recommendations_num='$daily_recommendations_num' WHERE user_id='$user_id'";

			$result = mysqli_query($con, $query);

			// Keeps checking whether the recommendation has been processed by the server
			// Redirect the user to show_recommendations page once it has been processed
			while(TRUE)
			{
				sleep(3); # To not overwhelm server with requests whilst processing the request

				$query = "SELECT complete FROM sync_requests WHERE user_id='$user_id' and complete=1 ORDER BY request_timestamp ASC LIMIT 1";

				$result = mysqli_query($con, $query);

				$result_arr = mysqli_fetch_assoc($result);

				if(!(is_null($result_arr)))
				{
					sleep(3);
					break;
				}
			}
			header("Location: show_recommendations.php");
			die;
		}
		else
		{
			echo("daily limit reached");
		}
	}
?>

<!-- Recommendations page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Recommendations</title>
	<link rel="stylesheet" href="css_files/recommendations_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="post">
			<div style="font-size: 20px;margin: 10px;color: white">Recommendations</div>
			<div class="inputBox">
				<input id="text" type="text" name="preferred_genre" required="required">
				<span>Preferred Genre (Enter * if any)</span>
				<i></i>
			</div>
			<br><br>
			<div class="links">
				<a href="index.php">Home Page</a>
				<a href="search_genres.php" class="float-end">Search Genres</a>
			</div>
			<br><br>
			<div class="slidecontainer">
				<span>How niche? (Left=Niche Right=Mainstream)</span>
				<br>
				<input type="range" min="1" max="10" value="5" required="required" name="slider_value" class="slider" id="myRange">
			</div>
			<br><br>
			<input id="button" type="submit" name="done" value="Submit">
		</form>
	</div>
</body>
</html>