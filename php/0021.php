<?php

include './functions.php';

function getAmicablePair($a){
    $da = array_sum(getDivisors($a)) - $a;
    $db = array_sum(getDivisors($da)) - $da;
    
    
    if($db == $a && $da != $a){
        return array($a,$da);
    }
    
    return false;
}

$sum = 0;

for($i = 220; $i < 10000; $i++){
    if($x = getAmicablePair($i)){
        $sum+=$x[0];
    }
}
echo $sum;