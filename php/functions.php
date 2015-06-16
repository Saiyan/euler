<?php

function logProgress($max,$step,$percentOnly = true,$append = ""){
    $end = 100 * $step /$max;
    if($percentOnly){
        $end = floor($end);
        echo "\r$end% $append";
        return;
    }else{
        $str = "";

        for($i = 0; $i < $end; $i++){
            $str .= ".";
        }
        for($i = 0; $i < 100 - $end; $i++){
            $str .= " ";
        }
        echo "\r[$str] $append";
    }
}

function getDivisors($z){
    $divisors = array(1,$z);
    $end = $z;
    for($j = 2; $j < $end; $j++){
        if(bcmod($z, $j) == 0){
            //Wenn eine Zahl ein teiler ist dann ist der Rest aus Zahl / Teiler auch ein Teiler. Somit muss die Schleife nur bis zu dem neuen Teiler laufen. (Zeitersparnis)
            array_push($divisors,$j);
            array_push($divisors,$z / $j);
            $end = $z / $j;
        }
    }
    return $divisors;
}