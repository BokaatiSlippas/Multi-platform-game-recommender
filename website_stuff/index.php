<?php
session_start();

	include("functions.php");

	// Connect to the users database
	$dbhost = "localhost";
	$dbuser = "root";
	$dbpass = "";
	$dbname = "users_db";

	$con = mysqli_connect($dbhost,$dbuser,$dbpass,$dbname);

	// Function to check if the user has logged in from functions.php
	$user_data = check_login($con);

?>

<!-- Index page design -->
<!DOCTYPE html>
<html lang="en" dir="ltr">
  	<head>
    	<meta charset="UTF-8">
    	<title>Arik's Games Recommender</title>
		<link rel="stylesheet" href="css_files/index_style.css">
    	<link href='https://unpkg.com/boxicons@2.0.7/css/boxicons.min.css' rel='stylesheet'>
     		<meta name="viewport" content="width=device-width, initial-scale=1.0">
   </head>
<body>
  	<div class="sidebar close">
    	<div class="logo-details">
      	<i class='bx bxl-medium-square'></i>
      	<span class="logo_name">Menu</span>
    	</div>
    	<ul class="nav-links">
	      	<li>
	        	<a href="find_similar_games.php">
	          		<i class='bx bx-grid-alt' ></i>
    	      		<span class="link_name">Find Similar Games</span>
        		</a>
        		<ul class="sub-menu blank">
          			<li><a class="link_name" href="find_similar_games.php">Find Similar Games</a></li>
	        	</ul>
    	  	</li>
      		<li>
        		<div class="icon-link">
          			<a href="#">
            			<i class='bx bx-collection' ></i>
            			<span class="link_name">Platforms</span>
          			</a>
          			<i class='bx bxs-chevron-down arrow' ></i>
        		</div>
        		<ul class="sub-menu">
          			<li><a class="link_name" href="#">Platforms</a></li>
          			<li><a href="steam_details.php">Steam</a></li>
					<li><a href="playtime.php">Manually Enter</a></li>
        		</ul>
      		</li>
      		<li>
        		<a href="games_list.php">
          			<i class='bx bx-list-ol'></i>
          			<span href="games_list.php" class="link_name">Games list</span>
        		</a>
        		<ul class="sub-menu blank">
          			<li><a class="link_name" href="games_list.php">Games-list</a></li>
        		</ul>
      		</li>
      		<li>
        		<a href="search_games.php">
          			<i class='bx bx-search-alt'></i>
          			<span href="search_games.php" class="link_name">Search Games</span>
        		</a>
        		<ul class="sub-menu blank">
          			<li><a class="link_name" href="search_games.php">Search Games</a></li>
        		</ul>
      		</li>
			<li>
        		<a href="search_genres.php">
					<i class='bx bx-bookmark-heart'></i>
          			<span href="search_genres.php" class="link_name">Search Genres</span>
        		</a>
        		<ul class="sub-menu blank">
          			<li><a class="link_name" href="search_genres.php">Search Genres</a></li>
        		</ul>
      		</li>
      		<li>
        		<a href="recommendations.php">
          			<i class='bx bx-happy-heart-eyes'></i>
          			<span href="recommendations.php" class="link_name">Recommendations</span>
        		</a>
        		<ul class="sub-menu blank">
          			<li><a class="link_name" href="recommendations.php">Recommendations</a></li>
        		</ul>
      		</li>
      		<li>
        		<div class="icon-link">
          			<a href="#">
            			<i class='bx bx-cog'></i>
            			<span class="link_name">Settings</span>
          			</a>
          			<i class='bx bxs-chevron-down arrow' ></i>
        		</div>
        		<ul class="sub-menu">
          			<li><a class="link_name" href="#">Settings</a></li>
          			<li><a href="change_password.php">Change Password</a></li>
          			<li><a href="logout.php">Logout</a></li>
        		</ul>
      		</li>
      		<li>
      			<a href="https://www.igdb.com/advanced_search">
				  	<i class='bx bxs-cube'></i>
          			<span class="link_name" href="https://www.igdb.com/advanced_search">IGDB website</span>
        		</a>
        		<ul class="sub-menu blank">
          			<li><a class="link_name" href="https://www.igdb.com/advanced_search">IGDB website</a></li>
        		</ul>
      		</li>
		</ul>
  	</div>
  	<section class="home-section">
  		<div class="home-content">
  			<i class="bx bx-menu"></i>
  			<span class="text">Sidebar</span>
  		</div>
  	</section>
  	<script>
	// Sidebar open
  	let arrow = document.querySelectorAll(".arrow");
  	for (var i = 0; i < arrow.length; i++) {
    		arrow[i].addEventListener("click", (e)=>{
   	let arrowParent = e.target.parentElement.parentElement;
   	arrowParent.classList.toggle("showMenu");
    		});
  	}

	// Sidebar close
  	let sidebar = document.querySelector(".sidebar");
  	let sidebarBtn = document.querySelector(".bx-menu");
  	console.log(sidebarBtn);
  	sidebarBtn.addEventListener("click", ()=>{
    	sidebar.classList.toggle("close");
  	});
  	</script>
</body>
</html>