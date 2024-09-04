<?php

session_start();

	if(isset($_POST["submit"]))
	{
		// Game was posted
		$game_name = $_POST["game_name"];

        $user_id = $_SESSION["user_id"];

		if(!empty($game_name))
		{
			// Connect to the games database
            $dbhost = "localhost";
            $dbuser = "root";
            $dbpass = "";
            $dbname = "games_db";

            $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

			$query = "SELECT id FROM games WHERE name='$game_name' LIMIT 1";
			$result = mysqli_query($con, $query);

		}else
		{
			echo "Please enter some valid information";
			echo "<script>setTimeout(\"location.href = 'find_similar_games.php';\",3000);</script>"; # displays error for 3000 milliseconds
		}

		// Check if the game exists
		if(mysqli_num_rows($result) === 0)
		{
			echo "Game name does not exist, go back and enter an actual game.";
			echo "<script>setTimeout(\"location.href = 'find_similar_games.php';\",3000);</script>"; # displays error for 3000 milliseconds
		}
        else
        {

            $result_arr = mysqli_fetch_assoc($result);
			
			$game_id = array_values($result_arr)[0];


			// Connect to the users database and upload the request for similar games
            $dbname = "users_db";

            $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

            $query = "INSERT INTO sync_requests (user_id,request_id,request_timestamp,request_int,request_int2,complete,server_output) VALUES ('$user_id',1,CURRENT_TIMESTAMP(),'$game_id',NULL,0,NULL)";

            $result = mysqli_query($con, $query);

            header("Location: show_similar_games.php");
        }
	}
	
?>


<!-- Find similar games page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Find Similar Games</title>
	<link rel="stylesheet" href="css_files/find_similar_games_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="post">
			<div style="font-size: 20px;margin: 10px;color: white">Game Name</div>
			<div class="inputBox">
				<input id="text" type="text" name="game_name" required="required">
				<span>Game Name</span>
				<i></i>
			</div>
			<br><br>
			<div class="links">
				<a href="index.php">Home Page</a>
				<a href="search_games.php" class="float-end">Search Games</a>
			</div>
			<br><br>
			<input id="button" type="submit" name="submit" value="Submit">
		</form>
	</div>
</body>
</html>