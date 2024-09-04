<!-- Game list page design -->
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Games List</title>
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
                                <header></header>
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
                                    <a href="search_list.php" class="float-end">Search Games Page</a>
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
                                    
	                                include("sidebar.html");
                                    // Connect to the games database
                                    $dbhost = "localhost";
                                    $dbuser = "root";
                                    $dbpass = "";
                                    $dbname = "games_db";

                                    $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

                                    // Get list of all games
                                    $query = "SELECT name,rating,rating_count,url FROM games ORDER BY rating_count desc, rating desc, name desc";

                                    $query_run = mysqli_query($con, $query);

                                    // Display all of the games in an ordered fashion
                                    foreach($query_run as $items)
                                    {
                                        ?>
                                        <tr>
                                            <td><?= $items['name']; ?></td>
                                            <td><?= (int)$items['rating']; ?></td>
                                            <td><?= (int)$items['rating_count']; ?></td>
                                            <td><a href="<?= $items['url']; ?>"><?= $items['url']; ?></a></td>
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