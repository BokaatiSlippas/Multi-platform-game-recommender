<!-- Show recommendations page design -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="css_files/show_recommendations_style.css" rel="stylesheet">
    <title>Show Recommendations</title>
</head>
<body>
    <?php
    session_start();

        include("functions.php");

        // Connect to the users database
        $dbhost = "localhost";
        $dbuser = "root";
        $dbpass = "";
        $dbname = "users_db";

        $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

        // Get the server output from the database
        $user_id = $_SESSION["user_id"];

        $query = "SELECT server_output FROM sync_requests WHERE complete=1 AND user_id='$user_id' ORDER BY request_timestamp ASC LIMIT 1";

        $result = mysqli_query($con, $query);

        $result_arr = mysqli_fetch_assoc($result);

        // Redirect the user back to the index page if they are trying to access without a recommendations request
        if(is_null($result_arr))
        {
            header("Location: index.php");
			die;
        }
        $game_id = array_values($result_arr)[0];


        // Connect to the games database
        $dbhost = "localhost";
        $dbuser = "root";
        $dbpass = "";
        $dbname = "games_db";

        $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

        // Get the game record outputted by the server
        $query = "SELECT name,parent_game,total_rating,total_rating_count,summary,url FROM games WHERE id='$game_id'";

        $result = mysqli_query($con, $query);

        $result_arr = mysqli_fetch_assoc($result);

        $output_arr = array_values($result_arr);

        $name = $output_arr[0];
        $parent_game = $output_arr[1];
        $total_rating = $output_arr[2];
        $total_rating_count = $output_arr[3];
        $summary = $output_arr[4];
        $url = $output_arr[5];

        ?>
        <h3>Game Name</h3><li style="font-weight:normal"><?= $name; ?></li>
        <br>
        <?php

        // Display all of the game record's information
        if(is_null($parent_game)){
            $parent_game_name = "Not Available";
        }
        else{
            $query = "SELECT name FROM games WHERE id='$parent_game'";
            $result = mysqli_query($con, $query);
            $result_arr = mysqli_fetch_assoc($result);
            $parent_game_name = array_values($result_arr)[0];
        }
        
        ?>
        <h3>Parent Game</h3><li style="font-weight:normal"><?= $parent_game_name; ?></l1>
        <br>
        <h3>Rating</h3><li style="font-weight:normal"><?= intval($total_rating); ?></li>
        <br>
        <h3>Rating Count</h3><li style="font-weight:normal"><?= $total_rating_count; ?></li>
        <br>
        <h3>Summary</h3><li style="font-weight:normal"><?= $summary; ?></li>
        <br>
        <h3>URL</h3><li style="font-weight:normal"><a href="<?= $url; ?>"><?= $url; ?></a></li>
        <br>
        <h3><?= "Game Engines"; ?></h3>
        <ul>

            <?php

            $query = "SELECT game_engine_id FROM link_games_game_engines WHERE game_id='$game_id'";

            $result = mysqli_query($con, $query);

            $result_arr = mysqli_fetch_assoc($result);

            if(is_null($result_arr)){
                ?><li><?= "None"; ?></li><?php
            }
            else{
                $game_engine_arr = array_values($result_arr);

                foreach($game_engine_arr as $game_engine_id)
                {
                    $query = "SELECT name FROM game_engines WHERE id='$game_engine_id'";

                    $result = mysqli_query($con, $query);

                    $game_engine_arr = mysqli_fetch_assoc($result);

                    if(!(is_null($game_engine_arr)))
                    {
                        $game_engine = array_values($game_engine_arr)[0];

                        ?><li><?= $game_engine; ?></li><?php
                    }
                    
                }
            }
            ?>

        </ul>
        <br>
        <h3><?= "Genres"; ?></h3>
        <ul>

            <?php

            $query = "SELECT genre_id FROM link_games_genres WHERE game_id='$game_id'";

            $result = mysqli_query($con, $query);

            $result_arr = mysqli_fetch_assoc($result);

            if(is_null($result_arr)){
                ?><li><?= "None"; ?></li><?php
            }
            else{
                $genre_arr = array_values($result_arr);

                foreach($genre_arr as $genre_id)
                {
                    $query = "SELECT name FROM genres WHERE id='$genre_id'";

                    $result = mysqli_query($con, $query);

                    $genre_arr = mysqli_fetch_assoc($result);

                    $genre = array_values($genre_arr)[0];

                    ?><li><?= $genre; ?></li><?php
                }
            }
            ?>
        
        </ul>
        <br>
        <h3><?= "Platforms"; ?></h3>
        <ul>

            <?php

            $query = "SELECT platform_id FROM link_games_platforms WHERE game_id='$game_id'";

            $result = mysqli_query($con, $query);

            $result_arr = mysqli_fetch_assoc($result);

            if(is_null($result_arr)){
                ?><li><?= "None"; ?></li><?php
            }
            else{
                $platform_arr = array_values($result_arr);

                foreach($platform_arr as $platform_id)
                {
                    $query = "SELECT name FROM platforms WHERE id='$platform_id'";

                    $result = mysqli_query($con, $query);

                    $platform_arr = mysqli_fetch_assoc($result);

                    $platform = array_values($platform_arr)[0];

                    ?><li><?= $platform; ?></li><?php
                }
            }
            ?>
        </ul>
        <div class="links">
            <h3><a href="index.php">Home Page</a></h3>
		</div>
</body>
</html>


<?php

    // Connect to the users database
    $dbhost = "localhost";
    $dbuser = "root";
    $dbpass = "";
    $dbname = "users_db";

    $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

    // Update the database to show the request has been completed
    $query = "UPDATE sync_requests SET complete=2 WHERE complete=1 AND user_id='$user_id' ORDER BY request_timestamp ASC LIMIT 1";

    $result = mysqli_query($con, $query);
?>