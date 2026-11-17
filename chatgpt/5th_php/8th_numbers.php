<?php
/* $a = 5;
$b = 5.34;
$c = "25";

var_dump($a);
var_dump($b);
var_dump($c); */

/* $x = 5985;
var_dump(is_int($x));

$y = 59.85;
var_dump(is_int(is_int($y))); */

/* $x = 10.365;
var_dump(is_float($x)); */

/* $x = 1.9e411;
var_dump(is_infinite($x)); */

/* $x = acos(8);
var_dump($x);

// Check if value is not a number (NaN)
var_dump(is_nan($x)); */

/* $x = 5985;
var_dump(is_numeric($x));

$x = "5985";
var_dump(is_numeric($x));
$x = "59.85" + 100;
var_dump(is_numeric($x));

$x = "Hello";
var_dump(is_numeric($x)); */

$x = 23465.768;
echo intval($x);

echo "<br>";

$x = "23465.768";
echo intval($x);
?>