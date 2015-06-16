<?php

$i=0;
$j=1;
$fib = 0;
$str_fib = "";
$c = 1;

while(strlen($str_fib) < 1000){
    $fib = gmp_add($i, $j);
    $c++;
    $i = $j;
    $j = $fib;
    $str_fib = gmp_strval($fib);
}

echo "The first term in the Fibonacci sequence to contain 1000 digits is: $c";