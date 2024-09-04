<?php
session_start();

	include("sidebar.html");

	$user_id = $_SESSION["user_id"];

	if(isset($_POST["submit"]))
	{
		$game_id = $_POST["game_id"];
        $playtime = $_POST["playtime"];

		if(!empty($game_id) && is_numeric($playtime) && is_numeric($game_id))
		{
			// Connect to the games database
			$dbhost = "localhost";
            $dbuser = "root";
            $dbpass = "";
            $dbname = "games_db";

			$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

			$query = "SELECT id FROM games WHERE id='$game_id'";
			$result = mysqli_query($con, $query);

			$result_arr = mysqli_fetch_assoc($result);

			// Check if the game id entered actually exists
			if(is_null($result_arr)){
				echo "The game does not exist enter the correct game id";
                echo "<script>setTimeout(\"location.href = 'playtime.php';\",3000);</script>"; # displays error for 3000 milliseconds
			}
			else{
				// Connect to the users database
				$dbhost = "localhost";
				$dbuser = "root";
				$dbpass = "";
				$dbname = "users_db";

				$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

				// Check if the user has already entered the game's playtime manually
				$query = "SELECT game_id from users_games WHERE user_id = '$user_id' and game_id = '$game_id'";
				$result = mysqli_query($con, $query);
				$result_arr = mysqli_fetch_assoc($result);

				if(is_null($result_arr)){
					$query = "INSERT INTO users_games (user_id,game_id,playtime) VALUES ('$user_id','$game_id','$playtime')";
					$query_run = mysqli_query($con, $query);
					?>
					<script type="text/javascript"> window.location.rel="noopener" target="_blank" href = 'index.php';>
					</script>
					<?php
				}
				else{
					echo "The game has already been entered by the user";
                	echo "<script>setTimeout(\"location.href = 'playtime.php';\",3000);</script>"; # displays error for 3000 milliseconds
				}
			}
		}
		else
		{
			echo("Please enter valid information");
            echo "<script>setTimeout(\"location.href = 'playtime.php';\",3000);</script>"; # displays error for 3000 milliseconds
		}
	}
?>

<!DOCTYPE html>
<html>
<head>
	<title>Game Playtime</title>
	<link rel="stylesheet" href="css_files/playtime_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="POST">
			<div style="font-size: 20px;margin: 10px;color: white">Enter playtime for a game</div>
			<div class="inputBox">
				<input id="text" type="text" name="game_id" required="required">
				<span>Game ID</span>
				<i></i>
			</div>
            <div class="inputBox">
				<input id="text" type="text" name="playtime" required="required">
				<span>Playtime in hours</span>
				<i></i>
			</div>
			<br>
			<div class="links">
				<a href="index.php">Home page</a>
			</div>
			<br>
			<input id="button" name="submit" type="submit" value="Submit">
		</form>
	</div>
</body>
</html>