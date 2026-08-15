<?php
// $x = 5;

// function myTest() {
//     echo "Variable x inside function is: $x";
// }
// myTest();

// echo "Variable x outside function is: $x";
// 

// function myTest() {
//     $x = 5;
//     echo "Variable x inside function is: $x";
// }
// myTest();

// echo "Variable x outside fnction is: $x";

// function myTest() {
//     static $x = 0;
//     echo $x;
//     $x++;
// }
// myTest();
// myTest();
// myTest();

// $x = 5;
// $y = 10;

// function myTest() {
//     global $x, $y;
//     $x = $x + $y;
// }
// myTest();
// echo $y;

$x = 5;
$y = 10;

function myTest() {
    $GLOBALS['y'] = $GLOBALS['x'] + $GLOBALS['y'];
}
myTest();
echo $y;
?>

