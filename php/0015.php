<?php

function getDreieck($size){
    $d = [];
    for($i = 0; $i < $size; $i++){
        $d[$i] = [];
        for($j = 0; $j < $i+1; $j++){
            if($j == 0 || $j == $i){
                $d[$i][$j] = 1;
            }else{
                $d[$i][$j] = 0;
            }
        }
    }
    return $d;
}

$size = 21;
$size2 = ($size-1) * 2 +1;
$dreieck = getDreieck($size2);

  for($i = 1; $i < count($dreieck);$i++){
      for($j = 1; $j < count($dreieck[$i]); $j++){
        
        if($dreieck[$i][$j] == 0){
            $dreieck[$i][$j] = $dreieck[$i-1][$j-1]  + $dreieck[$i-1][$j];
        }
    }
}

var_dump($dreieck[count($dreieck)-1]);
