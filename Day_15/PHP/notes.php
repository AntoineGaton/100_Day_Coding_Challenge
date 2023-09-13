<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <title>Playing Around With PHP</title>
</head>
<body>
   <?php
      // This is a single-line comment
      /*
      This is a multi-line comment
      It can span multiple lines.
      */

      // Variable declaration and assignment
      $name = "Antoine";
      $age = 35;
      $isDeveloper = true;

      // Outputting variables in HTML
      echo "<h1>Welcome, " . $name . "!</h1>";
      echo "<p>Your age is: " . $age . "</p>";

      // Conditional statement
      if ($isDeveloper) {
         echo "<p>You are a developer.</p>";
      } else {
         echo "<p>You are not a developer.</p>";
      }

      // Simple loop example
      for ($i = 1; $i <= 5; $i++) {
         echo "<p>Iteration #" . $i . "</p>";
      }

      // Array example
      $colors = ["red", "green", "blue"];
      echo "<ul>";
      foreach ($colors as $color) {
         echo "<li>" . $color . "</li>";
      }
      echo "</ul>";

      ?>
</body>
</html>