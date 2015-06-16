<?php

$x = pow(2, 1000);
$x = number_format($x,0,'','');
$sum = 0;

for($i = 0; $i < strlen($x); $i++){
    $sum += $x[$i];
}

echo $sum;