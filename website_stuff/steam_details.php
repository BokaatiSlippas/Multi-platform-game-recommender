<?php
session_start();

	include("functions.php");

	// Connect to the users database
    $dbhost = "localhost";
    $dbuser = "root";
    $dbpass = "";
    $dbname = "users_db";

    $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

	$user_data = check_login($con);

	$user_id = $user_data["user_id"];

	if(isset($_POST["submit"]))
	{
		// User steam id posted
		$user_steam_id = $_POST["user_steam_id"];

		if(!empty($user_steam_id) && is_numeric($user_steam_id) && strlen($user_steam_id)==17)
		{
			// Update user record with their steam id
			$query = "UPDATE users SET user_steam_id = '$user_steam_id' WHERE user_id = '$user_id'";
			$result = mysqli_query($con, $query);
			header("Location: index.php");
		}
		else
		{
			echo("Please enter valid details");
            echo "<script>setTimeout(\"location.href = 'steam_details.php';\",5000);</script>"; # displays error for 5000 milliseconds
		}
	}
?>

<!-- Steam detail page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Steam details</title>
	<link rel="stylesheet" href="css_files/steam_personal_details_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="POST">
			<div style="font-size: 20px;margin: 10px;color: white">Steam details</div>
			<div class="inputBox">
				<input id="text" type="text" name="user_steam_id" required="required">
				<span>Steam ID</span>
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