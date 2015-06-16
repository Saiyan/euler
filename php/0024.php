<?php 

function fillIn(&$arr,$number, $max,$pos=0){
    $k = $max;
    
    for($i=0; $k > 0;$i++){
        if($arr[$i][$k] == -1){
            $arr[$i][$k] = $number;
            $k--;
        }
    }
    
    
    
    //fillIn($arr,$number, $max,$pos+1);
}

$digits = [0,1,2];
$result = [];

for($i = 0; $i < count($digits); $i++){
    $result[$i] = array();
    for($j = 0; $j < count($digits); $j++){
        $result[$i][$j] = -1;
    }
}

fillIn($result,0, count($digits)-1);

var_dump($result);