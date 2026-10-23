<?php
// strlen
/* echo strlen("Hello world!"); */

// count words
/* echo str_word_count("Hello world!"); */

// search for the text love in the text
/* $txt = "I really love PHP!";
var_dump(str_contains($txt, "love")); */

// Search for the text "world" in the string "Hello world!":
/* echo strpos("Hello world!", "world"); */

// Check if a string starts with a specific substring:
/* $txt = "I really love PHP";
var_dump(str_starts_with($txt, "I really")); */

// Showing case-sensitivity:
/* $txt = "I really love PHP!";
var_dump(str_starts_with($txt, "i really")); */

// Check if a string ends with a specific substring:
/* $txt = "I really love PHP!";
var_dump(str_ends_with($txt, "PHP!"));
 */

$txt = "I really love PHP!";
var_dump(str_ends_with($txt, "php!"));
?>