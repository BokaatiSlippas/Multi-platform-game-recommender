<?php
    include("sidebar.html");
?>

<!-- Search games page design -->
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet">
    <title>Search Games</title>
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

                                <form action="" method="GET">
                                    <div class="input-group mb-3">
                                        <input type="text" name="search" required value="<?php if(isset($_GET['search'])){echo $_GET['search']; } ?>" class="form-control" placeholder="Search data">
                                        <button type="submit" class="btn btn-primary">Search</button>
                                    </div>
                                </form>

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
                                    <a href="index.php">Home page</a>
                                    <a href="find_similar_games.php" class="float-end">Find Similar Games</a>
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
                                    <th>Game ID</th>
                                </tr>
                            </thead>
                            <tbody>
                                <?php
                                    // Connect to the games database
                                    $dbhost = "localhost";
                                    $dbuser = "root";
                                    $dbpass = "";
                                    $dbname = "games_db";

                                    $con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

                                    if(isset($_GET['search']))
                                    {
                                        // Filter for the game searched
                                        $filtervalues = $_GET['search'];
                                        $query = "SELECT * FROM games WHERE CONCAT(name) LIKE '%$filtervalues%' ";
                                        $query_run = mysqli_query($con, $query);

                                        if(mysqli_num_rows($query_run) > 0)
                                        {
                                            foreach($query_run as $items)
                                            {
                                                ?>
                                                <!-- Display the games that fill the criteria -->
                                                <tr>
                                                    <td><?= $items['name']; ?></td>
                                                    <td><?= (int)$items['rating']; ?></td>
                                                    <td><?= (int)$items['rating_count']; ?></td>
                                                    <td><a href="<?= $items['url']; ?>"><?= $items['url']; ?></a></td>
                                                    <td><?= $items['id']; ?></td>
                                                </tr>
                                                
                                                <?php
                                            }
                                        }
                                        else
                                        {
                                            ?>
                                                <tr>
                                                    <td colspan="4">No Record Found</td>
                                                </tr>
                                            <?php
                                        }
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