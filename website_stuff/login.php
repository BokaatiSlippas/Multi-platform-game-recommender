<?php

session_start();

	include("functions.php");

	if(isset($_POST["login"]))
	{
		// User login details posted
		$user_name = $_POST["user_name"];
		$email = $_POST["email"];
		$password = $_POST["password"];

		// Connect to the users database
		$dbhost = "localhost";
		$dbuser = "root";
		$dbpass = "";
		$dbname = "users_db";

		$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

		if(!empty($user_name) && !empty($password) && !empty($email) && !is_numeric($user_name) && !is_numeric($email))
		{
			
			$query = "SELECT * FROM users WHERE email = '$email' AND user_name = '$user_name' LIMIT 1";
			$result = mysqli_query($con, $query);

		}else
		{

			echo "Please enter some valid information";
		}

		// Check if user record under email entered exists
		if(mysqli_num_rows($result) === 0)
		{
			die("Invalid details, go back and re-enter");
		}

		$user = mysqli_fetch_object($result);

		// Verify the password entered with the one in the user record in the database
		if(!password_verify($password, $user->password))
		{
			die("Password is not correct");
		}

		else if($user->email_verified_at == null)
		{
			die("Please verify your email <a href='email_verification.php?email=" . $email ."'>from here</a>");
		}
		else
		{
			// Session user_id is set which is necessary for the functionality of many pages
			$user_data = mysqli_fetch_assoc($result);
			$_SESSION["user_id"] = $user->user_id;
			header("Location: index.php");
			die;
			
		}
	}
	
?>

<!-- Login page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
	<link rel="stylesheet" href="css_files/login_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="post">
			<div style="font-size: 20px;margin: 10px;color: white">Login</div>
			<div class="inputBox">
				<input id="text" type="text" name="user_name" required="required">
				<span>Username</span>
				<i></i>
			</div>
			<div class="inputBox">
				<input id="text" type="text" name="email" required="required">
				<span>Email</span>
				<i></i>
			</div>
			<div class="inputBox">
				<input id="text" type="password" name="password" required="required">
				<span>Password</span>
				<i></i>
			</div>
			<br><br>
			<div class="links">
				<a href="signup.php">Signup page</a>
				<a href="forgot_password.php" class="float-end">Forgot Password</a>
			</div>
			<br><br>
			<input id="button" type="submit" name="login" value="Login">
		</form>
	</div>
</body>
</html>