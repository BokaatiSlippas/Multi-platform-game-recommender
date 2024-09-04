<?php


session_start();

	include("functions.php");

	use PHPMailer\PHPMailer\PHPMailer;
	use PHPMailer\PHPMailer\SMTP;
	use PHPMailer\PHPMailer\Exception;

	require "vendor/autoload.php";


	if(isset($_POST["continue"]))
	{
		// User details posted
		$user_name = $_POST["user_name"];
		$email = $_POST["email"];

		$mail = new PHPMailer(true);

		// Connect to the users database
		$dbhost = "localhost";
		$dbuser = "root";
		$dbpass = "";
		$dbname = "users_db";

		$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

        $query = "SELECT email FROM users WHERE email='$email'";
        $result = mysqli_query($con, $query);
		if(mysqli_num_rows($result))
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

				$mail->setFrom("bhuiyanparveena@gmail.com", "Arik-Bhuiyan-Parveen");

				$mail->addAddress($email, $user_name);

				$mail->isHTML(true);

				$verification_code = substr(number_format(time() * rand(), 0, "", ""), 0, 6);

				$mail->Subject = "Email verification";
				$mail->Body    = "<p>Your verification code for forgetting your password on Arik's Game Recommender is: <b style='font-size: 30px;'>" . $verification_code . "</b></p>";

				$mail->send();

                $query = "UPDATE users SET time_verification_code_sent = NOW(), verification_code='$verification_code' WHERE email = '$email' AND user_name = '$user_name'";

                mysqli_query($con, $query);


				if(!empty($user_name) && !empty($email))
				{

					echo "Email sent to {$email}";

					header("Location: forgot_password_email_verification.php?email=" . $email);

					exit();
				}else
				{

					echo "Please enter some valid information";
				}

			} catch (Exception $e) {
				echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo} ";
			}
		}
		else
		{
			echo "Email not associated with an account";
		}
		
	}
?>

<!-- Forgot password page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Forgot Password</title>
	<link rel="stylesheet" href="css_files/forgot_password_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="post">
			<div style="font-size: 20px;margin: 10px;color: white">Forgot Password</div>
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
			<br><br>
			<div class="links">
				<a href="signup.php">Signup page</a>
				<a href="login.php" class="float-end">Login page</a>
			</div>
			<br><br>
			<input id="button" type="submit" name="continue" value="Continue">
		</form>
	</div>
</body>
</html>