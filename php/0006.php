<?php

$sum_of_squares = 0;
$sums = 0;
$square_of_sums;

for($i = 1; $i <= 100; $i++){
    $sum_of_squares+= pow($i,2);
    $sums+=$i;
}

$square_of_sums = pow($sums,2);

echo "$sum_of_squares\r\n";
echo "$square_of_sums\r\n";


echo $sum_of_squares - $square_of_sums;