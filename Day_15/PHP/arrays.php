<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link rel="stylesheet" href="style.css">
   <title>Index HTML</title>
</head>
<body>
   <h1><? bloginfo('name'); ?></h1>
   <h2><? bloginfo('description'); ?></h2>

   <? 
      echo "<p>List of colors</p>";
      $colors = array("red", "green", "blue");
      for ($i = 0; $i < count($colors); $i++){
         echo "<li> $colors[$i]</li>"; 
      }

      echo "<p>My Info</p>";
      $person = [
         "first name" => "Antoine", 
         "last name" => "Gaton",
         "age" => 35,
      ];
      foreach ($person as $key => $p){
         echo "<li> $key : $p</li>";
      }
   ?>
   
</body>
</html>