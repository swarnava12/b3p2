
    <script src="http://code.jquery.com/jquery-1.11.0.min.js"></script>     <!-- link to the jQuery library (see http://jquery.com) -->
	
	<!-- you can use these links, but better you have a link to the versions you need -->
    <!-- usage of folder "current" is not recommended -->
    <!-- see http://beaverslider.com/how-to-setup/docs/general for more info -->
    <script src="http://beaverslider.com/code/current/beaverslider.js"></script>         <!-- link to a framework -->
	<script src="http://beaverslider.com/code/current/beaverslider-effects.js"></script> <!-- link to a set of effects -->
	
	<!-- if you want to make styling link some css files -->
    
	<script>
	
	$(function(){
      var slider = new BeaverSlider({
        structure: {
          container: {
            id: "my-slider",
            width: 720,
            height: 420
          }
        },
        content: {
          images: [
            "img/1.jpg",
            "img/2.jpg"
          ]
        },
        animation: {
          effects: effectSets["slider: big set 1"],
          interval: 1000
        }
      });   
	});
	
	</script>
  </head>


    <div id="my-slider"></div>
