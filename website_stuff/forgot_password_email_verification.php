<?php

session_start();

	include("functions.php");

	if(isset($_POST["verify_email"]))
	{
		$email = $_POST["email"];
		$verification_code = $_POST["verification_code"];
        $new_password = $_POST["new_password"];

        $encrypted_password = password_hash($new_password, PASSWORD_DEFAULT);

		if(!empty($email) && !empty($verification_code))
		{
			// Connect to the users database
			$dbhost = "localhost";
			$dbuser = "root";
			$dbpass = "";
			$dbname = "users_db";

			$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

			$query = "SELECT verification_code FROM users WHERE email='$email' ORDER BY user_id DESC LIMIT 1";

			$result = mysqli_query($con, $query);
			$result_arr = mysqli_fetch_assoc($result);

			$database_verification_code = array_values($result_arr)[0];
			
			// Check if the verification code entered matches with the one in the database (the one that was sent)
			if($database_verification_code == $verification_code)
			{
				$query = "UPDATE users SET email_verified_at = NOW(), password = '$encrypted_password' WHERE email = '$email' AND verification_code = '$verification_code'";
				mysqli_query($con, $query);
				header("Location: login.php");
			}
			else{
				die("Wrong verification code was entered, go back and re-verify");
			}
		}
		else
		{

			echo "Please enter a verification code";
		}

		if(mysqli_affected_rows($con) == 0)
		{
			die("Verification code failed.");
		}

		echo "<p>You can login now.</p>";
		exit();
	}

?>

<!-- Forgot password email verification page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Forgot Password Email verification</title>
	<link rel="stylesheet" href="css_files/forgot_password_email_verification_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="POST">
			<div style="font-size: 20px;margin: 10px;color: white">Verify email</div>
			<input id="text" type="hidden" name="email" value="<?php echo $_GET['email']; ?>" required="required">
			<div class="inputBox">
				<input id="text" type="text" name="verification_code" required="required">
				<span>Verification code</span>
				<i></i>
			</div>
            <div class="inputBox">
				<input id="text" type="password" name="new_password" required="required">
				<span>New Password</span>
				<i></i>
			</div>
			<br><br>
			<br><br>
			<input id="button" type="submit" name="verify_email" value="Verify Email">
		</form>
	</div>
</body>
</html>