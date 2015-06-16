<?php

function isPrime($z){
    if($z === 2) return true;
    if(bcmod($z, 2) == 0) return false;
    $max =  floor(sqrt($z));
    for($i = 3; $i <= $max; $i+=2){
        if(bcmod($z, $i) == 0) return false;
    }
    return true;
}

$sum = 0;
$max = 2000000;
$p = 0;

for($i = 2; $i < $max; $i++){
    if(bcmod($i, 20000) == 0) echo "\r".++$p."%";
    if(isPrime($i)){
        $sum+=$i;
    }
}
echo "\007"; // SOUND
echo "\r\n$sum";


