<?php

include './functions.php';

$highest = 0;
$number = 0;
function NextCollatz($z){
    if($z == 1) return 1;
    if(bcmod($z,2) == 0){
        return NextCollatz($z/2)+1;
    }else{
        return NextCollatz(3*$z+1)+1;
    }
}

for($i = 13; $i < 1000000; $i++){
    $x = NextCollatz($i);
    
    if($i % 10000 == 0){
        logProgress(1000000, $i,true);
    }
    
    if($x > $highest){
        $highest = $x;
        $number = $i;
    }
}

echo "Number: $number with $highest terms";

