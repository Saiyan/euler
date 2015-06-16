<?php

$zahl = 1;
do{
    $next = false;
    $zahl++;
    for($i=1; $i <= 20;$i++){
        if($zahl % $i != 0){
            $next = true;
            break;
        }
    }
}while($next);

echo $zahl;