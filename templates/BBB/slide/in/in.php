<script src="js/jquery-1.11.0.js"></script>
<script src="js/bootstrap.min.js"></script>

  <link rel="stylesheet" href="css/bootstrap.min.css">

  <link rel="stylesheet" href="css/half-slider.css">
  
  <div style="width:600px;">
	<header id="myCarousel" class="carousel slide" style="height: 296px" >
        <!-- Indicators -->
        <ol class="carousel-indicators">
            <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
            <li data-target="#myCarousel" data-slide-to="1"></li>
            <li data-target="#myCarousel" data-slide-to="2"></li>
            <li data-target="#myCarousel" data-slide-to="3"></li>
            <li data-target="#myCarousel" data-slide-to="4"></li>
            <li data-target="#myCarousel" data-slide-to="5"></li>
        </ol>

        <!-- Wrapper for Slides -->
        <div class="carousel-inner">
            <div class="item active">
                <!-- Set the first background image using inline CSS below. -->
                <div class="fill" style="background-image:url('img/uoh/1.jpg');"></div>
                <div class="carousel-caption">
                    <h4>University of Hyderabad</h4>
                </div>
            </div>
            <div class="item">
                <!-- Set the second background image using inline CSS below. -->
                <div class="fill" style="background-image:url('img/uoh/3.jpg');"></div>
                <div class="carousel-caption">
                    <h4>University of Hyderabad</h4>
                </div>
            </div>
            <div class="item">
                <!-- Set the third background image using inline CSS below. -->
                <div class="fill" style="background-image:url('img/uoh/2.jpg');"></div>
                <div class="carousel-caption">
                    <h4>University of Hyderabad</h4>
                </div>
            </div>
			<div class="item">
                <!-- Set the third background image using inline CSS below. -->
                <div class="fill" style="background-image:url('img/uoh/4.jpg');"></div>
                <div class="carousel-caption">
                    <h4>University of Hyderabad</h4>
                </div>
            </div>
			<div class="item">
                <!-- Set the third background image using inline CSS below. -->
                <div class="fill" style="background-image:url('img/uoh/5.jpg');"></div>
                <div class="carousel-caption">
                    <h4>University of Hyderabad</h4>
                </div>
            </div>
			<div class="item">
                <!-- Set the third background image using inline CSS below. -->
                <div class="fill" style="background-image:url('img/uoh/6.jpg');"></div>
                <div class="carousel-caption">
                    <h4>University of Hyderabad</h4>
                </div>
            </div>
        </div>

        <!-- Controls -->
        <a class="left carousel-control" href="#myCarousel" data-slide="prev">
            <span class="icon-prev"></span>
        </a>
        <a class="right carousel-control" href="#myCarousel" data-slide="next">
            <span class="icon-next"></span>
        </a>

    </header>
		    <!-- Bootstrap Core JavaScript -->
 
</div>
    <!-- Script to Activate the Carousel -->
    <script>
    $('.carousel').carousel({
        interval: 2000 //changes the speed
    })
    </script>	