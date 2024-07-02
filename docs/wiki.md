<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NCOR Document Acts Working Group</title>
<style>
  body {
    position: relative;
    margin: 0;
    background: transparent;
    color: #000; /* Black text */
    height: 100vh;
    overflow: hidden; /* Prevents scrolling */
  }
  body::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('https://raw.githubusercontent.com/johnbeve/NCOR-Test/main/docs/logos/semantic-web-stack.png');
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
    opacity: 0.05; /* Lighten the background */
    z-index: -1;
  }
  h1, h2, p, a, li {
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Text shadow for better readability */
  }
  .custom-color {
    color: #0056b3; 
    transition: color 0.3s; /* Smooth transition for color change */
  }
  /* Change color when hovering */
  .custom-color:hover {
    color: #003580; /* Darker shade of the original color */
  }
  iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
  }
</style>
</head>
<body>
<h1>NCOR Wiki</h1>
<iframe src="https://ncorwiki.buffalo.edu/index.php/Main_Page"></iframe>
</body>
</html>
