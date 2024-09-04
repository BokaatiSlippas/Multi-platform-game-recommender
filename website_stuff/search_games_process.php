<?php
session_start();

	include("sidebar.html");

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Game name posted
        $game_name = $_POST['button_value'];

        $user_id = $_SESSION["user_id"];

        // Connect to the games database
        $dbhost = "localhost";
        $dbuser = "root";
        $dbpass = "";
        $dbname = "games_db";

        // Process for finding the game
        $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

        $query = "SELECT id FROM games WHERE name='$game_name'";

        $result = mysqli_query($con, $query);

        $result_arr = mysqli_fetch_assoc($result);

        $game_id = array_values($result_arr)[0];

        $dbname = "users_db";

        // Upload the request onto the database
        $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

        $query = "INSERT INTO sync_requests (user_id,request_id,request_timestamp,request_int,complete,server_output) VALUES ('$user_id',2,CURRENT_TIMESTAMP(),'$game_id',0,NULL)";

        $result = mysqli_query($con, $query);

        header("Location: show_similar_games.php");
        die;
    }
?>