<?php

// Function to check if the user has logged in or not otherwise they are re-directed to login page
function check_login($con)
{


	if(isset($_SESSION["user_id"]))
	{

		$user_id = $_SESSION["user_id"];
		$query = "select * from users where user_id = '$user_id' limit 1";

		$result = mysqli_query($con,$query);
		if($result && mysqli_num_rows($result) > 0)
		{

			$user_data = mysqli_fetch_assoc($result);
			return $user_data;
		}
	}

	//redirect to login
	header("Location: login.php");
	die;

}
?>