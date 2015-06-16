<?php
echo "\n";

function isPrime($z){
    for($i = 2; $i < $z/2; $i++){
        if($z % $i == 0) return false;
    }
    return true;
}

$zahl = 600851475143;
$highest = 0;
$produkt = 0;
$i = 2;
while($i++){
    if(bcmod($zahl, $i) == 0){
        $produkt = $produkt ? $produkt*$i : $i;
    }
    if($produkt == $zahl){
        echo "$i \r\n";
        break;
    }
}