<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="style.css">
   <title>Index HTML</title>
</head>
<body>
   <h1><? bloginfo(); ?></h1>
   <h2><? bloginfo('description'); ?></h2>

   <? 
      function myFirstPHPFunction($name, $color) {
         echo "Hello World! My name is $name and my favorite color is $color.";
         echo "<br>";
      }
      myFirstPHPFunction("Antoine", "blue");
   ?>
   
   <p><?php myFirstPHPFunction("Bianca", "pink"); ?></p>
</body>
</html>