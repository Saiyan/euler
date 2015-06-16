<?php

$sum = 0;
$fib = 0;
$i = 0;
$j = 1;

while($fib <= 4000000){
    $fib = $i+$j;
    $i = $j;
    $j = $fib;
    if($fib % 2 == 0)
        $sum+=$fib;
}

echo $sum;