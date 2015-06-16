<?php
function isPalindrome($z){
    for($i=0,$j=strlen($z)-1; $i<$j; $i++,$j--){
        if(!($z[$i] == $z[$j])) return false;
    }
    return true;
}
$highest = 0;
for($digit1=999; $digit1 > 99; $digit1--){
    for($digit2=999; $digit2 > 99; $digit2--){
        $product = (string)($digit1*$digit2);
        if(strlen($product) % 2 == 0 && isPalindrome($product)){
            if($highest < $product)$highest = $product;
        }
    }
}
echo $highest;