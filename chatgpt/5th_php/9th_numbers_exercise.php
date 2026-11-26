<?php
/* Inside the editor, complete the following steps:
Create $a with the integer 5 and $b with the float 5.34
Use var_dump() with is_int() to check if $a is an integer
Then print the integer value of $b with intval() (use echo)
The program should print two lines:
bool(true)
5 */
$a = 5;
$b = 5.34;

var_dump(is_int($a));
echo intval($b);
?>