<!DOCTYPE HTML>

<html>
    <div id="featuredfull">
	<head>
		<title>Dublin Bikes</title>
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<meta name="description" content="" />
		<meta name="keywords" content="" />
		<link href='http://fonts.googleapis.com/css?family=Roboto:400,100,300,700,500,900' rel='stylesheet' type='text/css'>
		<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
		<script src="js/skel.min.js"></script>
		<script src="js/skel-panels.min.js"></script>
		<script src="js/init.js"></script>

	</head>
	<body class="homepage">
        


	<!-- Header -->
        <div id="featuredxx">

        <iframe src="https://www.google.com/maps/embed?pb=!1m14!1m12!1m3!1d38114.079780167594!2d-6.272818401459338!3d53.34092930223022!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!5e0!3m2!1sen!2sie!4v1489437979992" width="1800" height="570" frameborder="0" style="border:0" allowfullscreen></iframe>

			</div>
		</div>

	<!-- Featured -->
		<div id="featured">
             <div id="featuredx">
			<div class="container">
				<header>
                   
					<h2>Hello.</h2>
                    
				</header>
                <p> 
                    We have the latest Dublin Bikes Info - Free for everyone  </p>
                
                
                            <?php
 
                                $servername = "dublinbikesmysql.cqcpf75mkbbq.us-west-2.rds.amazonaws.com";
                                $username = "DavidSurridge";
                                $password = "MyGerryAdams";

                                // Create connection
                                $conn = new mysqli($servername, $username, $password);

                                // Check connection
                                if ($conn->connect_error) {
                                    die("Uh oh! Service Offline | Please Try Again Later! " . $conn->connect_error);
                                } 
                                echo "Service Online ✓ | Select a Station Below (or a Zone Above) " . "<br>";
                            ?>
				<hr />	                   
                </div>
                </div>
       
                            <?php
                
                                $sql = "SELECT * FROM myDublinBikes.bikes_dynamic, myDublinBikes.bikes_static;";
                                $result = mysqli_query($conn, $sql);

                                if (mysqli_num_rows($result) > 0) {
                                // output data of each row
                                while($row = mysqli_fetch_assoc($result)) {
                                echo "Station Address: " . $row["address"]. "<br>" .  
                                    "Station Status: " . $row["status"]. "<br>" . "  Available Stands: " . $row["available_bike_stands"]. "<br>". "  Available Bikes: " . $row["available_bikes"]. "<br>". "<br>";
                                }
                                } else {
                                            echo "0 results";
                                }
                                mysqli_close($conn);
                            ?>
		
                </div>

	</body>
    </div>
</html>