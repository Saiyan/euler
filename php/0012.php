<?php

include 'functions.php';

function getTriangleByNr($z){
    return (($z+1)*$z)/2;
}


$highestCount = 1;

for($i=1; true; $i++){
    $t = getTriangleByNr($i);
    
    $divisors = getDivisors($t);
    $dcount = count($divisors);
    
    if($dcount > 500){
        $str = "$t";
        echo $str;
        return;
    }
}