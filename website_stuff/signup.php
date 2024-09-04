<?php


session_start();
	
	include("functions.php");

	use PHPMailer\PHPMailer\PHPMailer;
	use PHPMailer\PHPMailer\SMTP;
	use PHPMailer\PHPMailer\Exception;

	require "vendor/autoload.php";
	
	if(isset($_POST["signup"]))
	{
		// User singup details were posted
		$user_name = $_POST["user_name"];
		$password = $_POST["password"];
		$re_password = $_POST["re_password"];
		$email = $_POST["email"];

		// User record created in database if passes all tests

		// Connect to the database
		$dbhost = "localhost";
		$dbuser = "root";
		$dbpass = "";
		$dbname = "users_db";

		$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

		//First test is to ensure the username isn't already taken
		$query = "SELECT user_name FROM users WHERE user_name = '$user_name'";
		$result = mysqli_query($con, $query);

		$result_arr = mysqli_fetch_assoc($result);

		if(!(is_null($result_arr)))
		{
			die("The username already exists. Please go back and enter new details.");
		}

		$mail = new PHPMailer(true);

		// Second test is to validate the email
		if (!filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
		} else { 
			die("$email is not a valid email address, go back and re-enter new details"); 
		}

		// The final test is seeing if the passwords are the same, if they are can proceed
		if($password === $re_password)
		{
			// Set of code for sending the verification mail to the user
			try{

				$mail->SMTPDebug = 0;

				$mail->isSMTP();

				$mail->Host = "smtp.gmail.com";

				$mail->SMTPAuth = true;

				$mail->Username = "bhuiyanparveena@gmail.com";

				$mail->Password = "gnyjkssedbpeywjn";

				$mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;

				//TCP port to connect to 587
				$mail->Port = 587;

				$mail->setFrom("bhuiyanparveena@gmail.com", "Game Recommender");

				$mail->addAddress($email, $user_name);

				$mail->isHTML(true);

				$verification_code = substr(number_format(time() * rand(), 0, "", ""), 0, 6);

				$mail->Subject = "Email verification";
				$mail->Body    = "<p>Your account verification code for the Game Recommender is: <b style='font-size: 30px;'>" . $verification_code . "</b></p>";

				$mail->send();

				// Hashed password is stored in the database, any further password checks are done via re-hasing the password entered
				$encrypted_password = password_hash($password, PASSWORD_DEFAULT);
				if(!empty($user_name) && !empty($password) && !empty($email) && !is_numeric($user_name) && !is_numeric($email))
				{

					// Save record to database
					$query = "SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1";
					$result = mysqli_query($con, $query);
					$user_id_arr = mysqli_fetch_assoc($result);
					if(is_null($user_id_arr)){
						$user_id_previous = -1;
					}
					else{
						$user_id_previous = array_values($user_id_arr)[0];
					}
					$user_id = $user_id_previous + 1;
					$query = "INSERT INTO users (user_id,user_name,password,email,verification_code,status,email_verified_at,date,pro_package,daily_recommendations_num,user_steam_id) VALUES ('$user_id','$user_name','$encrypted_password','$email','$verification_code',NULL,NULL,CURRENT_TIMESTAMP(),0,3,NULL)";

					mysqli_query($con, $query);

					header("Location: email_verification.php?email=" . $email);
					exit();
				}else
				{
					echo "Please enter some valid information";
					echo "<script>setTimeout(\"location.href = 'signup.php';\",3000);</script>"; # displays error for 3000 milliseconds
				}

			} catch (Exception $e) {
				echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo} ";
				echo "<script>setTimeout(\"location.href = 'signup.php';\",3000);</script>"; # displays error for 3000 milliseconds
			}
		}
		else
		{
			echo "Passwords are not the same";
			echo "<script>setTimeout(\"location.href = 'signup.php';\",3000);</script>"; # displays error for 3000 milliseconds
		}
		
	}
?>

<!-- Singup page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Signup</title>
	<link rel="stylesheet" href="css_files/signup_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="POST">
			<div style="font-size: 20px;margin: 10px;color: white">Signup</div>
			<div class="inputBox">
				<input id="text" type="text" name="user_name" required="required">
				<span>Username</span>
				<i></i>
			</div>
			<div class="inputBox">
				<input id="email" type="text" name="email" required="required" onkeydown="validation()">
				<span id="email">Email</span>
				<i></i>
			</div>
			<div class="inputBox">
				<input id="text" type="password" name="password" required="required">
				<span>Password</span>
				<i></i>
			</div>
			<div class="inputBox">
				<input id="text" type="password" name="re_password" required="required">
				<span>Confirm Password</span>
				<i></i>
			</div>
			<br><br>
			<div class="links">
				<a href="login.php">Login page</a>
			</div>
			<br>
			<input id="button" type="submit" name="signup" value="Signup">
		</form>
	</div>
</body>
</html>