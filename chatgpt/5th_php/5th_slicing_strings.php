<?php
// Start the slice at index 6 and end the slice 5 positions later:
/* $x = "Hello World!";
echo substr($x, 6, 5); */

// Start the slice at index 6 and go all the way to the end:
/* $x = "Hello World!";
echo substr($x, 6); */

// Get the 3 characters, starting from the "o" in world (index -5):
/* $x = "Hello World!";
echo substr($x, -5, 3); */

// Should end up with "ow are y":
/* $x = "Hi, how are you?";
echo substr($x, 5, -3); */

//
?>