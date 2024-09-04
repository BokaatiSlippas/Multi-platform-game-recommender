<?php

session_start();

    sleep(3);

    // Connect to the users database
    $dbhost = "localhost";
    $dbuser = "root";
    $dbpass = "";
    $dbname = "users_db";

    $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

    $user_id = $_SESSION["user_id"];

    // Get similar games requests
    $query = "SELECT request_int FROM sync_requests WHERE complete=0 AND request_id=1 AND user_id='$user_id' ORDER BY request_timestamp ASC LIMIT 1";

    $result = mysqli_query($con, $query);

    $result_arr = mysqli_fetch_assoc($result);

    // If no request has been made the user is redirected to the index page
    if(is_null($result_arr))
    {
        header("Location: index.php");
        die;
    }
    $game_id = array_values($result_arr)[0];

    // Connect to the games database
    $dbname = "games_db";

    $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

    // Get the game record
    $query = "SELECT name FROM games WHERE id='$game_id'";

    $result = mysqli_query($con, $query);

    $result_arr = mysqli_fetch_assoc($result);

    $game_name = array_values($result_arr)[0];




    //$query = "SELECT similar_game_id FROM link_games_similar_games WHERE game_id='$game_id'";

    //$result = mysqli_query($con, $query);

    //$result_arr = mysqli_fetch_assoc($result);

    //if(is_null($result_arr))
    //{
    //    $similar_games_arr = [];
    //}
    //else
    //{
    //    $similar_games_arr = $result_arr;
    //}

?>

<!-- Show similar games page design -->
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Similar Games</title>
</head>
<body>

    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="card mt-4">
                    <div class="card-header">
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-7">
                                <header>Similar games to <?= $game_name; ?></header>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-12">
                <div class="card mt-4">
                    <div class="card-header">
                    </div>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-md-7">
                                <div class="links">
                                    <a href="index.php" class="float-beginning">Home page</a>
                                    <a href="search_games.php" class="float-end">Search Games Page</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-12">
                <div class="card mt-4">
                    <div class="card-body">
                        <table class="table table-bordered">
                            <thead>
                                <tr>
                                    <th>Game</th>
                                    <th>Rating</th>
                                    <th>Rating Count</th>
                                    <th>Game URL</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php
                                    $query = "SELECT similar_game_id FROM link_games_similar_games WHERE game_id='$game_id'";
                                    $query_run = mysqli_query($con, $query);
                                    if(mysqli_num_rows($query_run) > 0)
                                    {
                                        foreach($query_run as $items)
                                        {
                                            $similar_game_id = $items["similar_game_id"];

                                            $query = "SELECT name,rating,rating_count,url FROM games WHERE id='$similar_game_id'";

                                            $result = mysqli_query($con, $query);

                                            $result_arr = mysqli_fetch_assoc($result);
                                            try {
                                                if (is_array($result_arr)) {
                                                    $items = array_values($result_arr);
                                                    ?>
                                                    <tr>
                                                        <td><?= $items[0]; ?></td>
                                                        <td><?= (int)$items[1]; ?></td>
                                                        <td><?= (int)$items[2]; ?></td>
                                                        <td><a href="<?= $items[3]; ?>"><?= $items[3]; ?></a></td>
                                                    </tr>
                                                    <?php
                                                }
                                            } catch (Exception $e) {
                                            }
                                        }
                                    }
                                    else
                                    {
                                        ?>
                                        <tr>
                                            <td>No Similar Games</td>
                                        </tr>
                                        <?php
                                    }
                                ?>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.5.1.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
<?php

    $dbhost = "localhost";
    $dbuser = "root";
    $dbpass = "";
    $dbname = "users_db";

    $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

    $query = "UPDATE sync_requests SET complete=2 WHERE complete=0 AND user_id='$user_id' ORDER BY request_timestamp ASC LIMIT 1";

    $result = mysqli_query($con, $query);

?>