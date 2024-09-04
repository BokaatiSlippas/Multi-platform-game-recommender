<?php

session_start();

	include("functions.php");

	//The section below just verifies the old password and compares the new passwords and upon success updates it on the database

	if(isset($_POST["submit"]))
	{
		$old_password = $_POST["old_password"];
		$new_password = $_POST["new_password"];
		$verify_new_password = $_POST["verify_new_password"];

        

		if(!empty($old_password) && !empty($new_password) && !empty($verify_new_password))
		{

            $user_id = $_SESSION["user_id"];

			// Connect to the users database
			$dbhost = "localhost";
			$dbuser = "root";
			$dbpass = "";
			$dbname = "users_db";

			$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

            $query = "SELECT * FROM users WHERE user_id = '$user_id'";
            $result = mysqli_query($con, $query);

            $user = mysqli_fetch_object($result);

            if(!password_verify($old_password, $user->password))
            {
				echo "The old password does not match";
                echo "<script>setTimeout(\"location.href = 'change_password.php';\",3000);</script>"; # displays error for 3000 milliseconds
            }
            else if($new_password !== $verify_new_password)
            {
				echo "The new passwords do not match";
                echo "<script>setTimeout(\"location.href = 'change_password.php';\",3000);</script>"; # displays error for 3000 milliseconds
            }
            else
            {
                $encrypted_password = password_hash($new_password, PASSWORD_DEFAULT);

                $query = "UPDATE users SET password='$encrypted_password' WHERE user_id='$user_id'";
                $result = mysqli_query($con, $query);
                header("Location: index.php");
			    die;
            }
        }
        else
        {
            echo "Fill in all the boxes";
            echo "<script>setTimeout(\"location.href = 'change_password.php';\",3000);</script>"; # displays error for 3000 milliseconds
        }
	}
	
?>

<!-- Change password page design -->
<!DOCTYPE html>
<html>
<head>
	<title>Change Password</title>
	<link rel="stylesheet" href="css_files/change_password_style.css">
</head>
<body>
	<div class="box" id="box">
		<span class="borderLine"></span>
		<form method="post">
			<div style="font-size: 20px;margin: 10px;color: white">Change Password</div>
			<div class="inputBox">
				<input id="text" type="password" name="old_password" required="required">
				<span>Old Password</span>
				<i></i>
			</div>
			<div class="inputBox">
				<input id="text" type="password" name="new_password" required="required">
				<span>New Password</span>
				<i></i>
			</div>
			<div class="inputBox">
				<input id="text" type="password" name="verify_new_password" required="required">
				<span>Verify New Password</span>
				<i></i>
			</div>
			<br><br>
			<div class="links">
				<a href="index.php">Home page</a>
			</div>
			<br><br>
			<input id="button" type="submit" name="submit" value="Submit">
		</form>
	</div>
</body>
</html>