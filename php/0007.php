<?php

function isPrime($z){
    for($i = 2; $i < $z/2; $i++){
        if($z % $i == 0) return false;
    }
    return true;
}

$counter = 1;
$result = 0;

for($i=3; $counter < 10001; $i+=2){
    if(isPrime($i)){
        echo "$counter\r\n";
        $result = $i;
        $counter++;
    }
}

echo "---$result---";