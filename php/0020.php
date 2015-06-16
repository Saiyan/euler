<?php

function fact($n){
    $res = $n;
    $n-=1;
    while($n > 0){
        $res*=$n--;
    }
    return $res;
}
$n = 100;
$f = fact($n);

$fs = number_format($f, 0, '', '');
$sum = 0;

for($i = 0; $i < strlen($fs);$i++){
    (int)$sum += (int)$fs[$i];
}


echo "$n! = $fs\r\n";
echo $sum;
