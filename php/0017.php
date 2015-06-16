<?php


function getNumberAsText($n){
    if($n > 1000 || $n < 0) return "ERROR";
    $str = "";
    
    if((int)$n < 21){
        switch($n){
            case 1:
                return "one";
            case 2:
                return "two";
            case 3:
                return "three";
            case 4:
                return "four";
            case 5:
                return "five";
            case 6:
                return "six";
            case 7:
                return "seven";
            case 8:
                return "eight";
            case 9:
                return "nine";
            case 10:
                return "ten";
            case 11:
                return "eleven";
            case 12:
                return "twelve";
            case 13:
                return "thirteen";
            case 14:
                return "fourteen";
            case 15:
                return "fifteen";
            case 16:
                return "sixteen";
            case 17:
                return "seventeen";
            case 18:
                return "eighteen";
            case 19:
                return "nineteen";
            case 20:
                return "twenty";
        }
    }else if($n < 30){
        $str.="twenty-".getNumberAsText($n-20);
    }else if($n < 40){
        $str.="thirty-".getNumberAsText($n-30);
    }else if($n < 50){
        $str.="forty-".getNumberAsText($n-40);
    }else if($n < 60){
        $str.="fifty-".getNumberAsText($n-50);
    }else if($n < 70){
        $str.="sixty-".getNumberAsText($n-60);
    }else if($n < 80){
        $str.="seventy-".getNumberAsText($n-70);
    }else if($n < 90){
        $str.="eighty-".getNumberAsText($n-80);
    }else if($n < 100){
        $str.="ninety-".getNumberAsText($n-90);
    }else if($n < 1000){
        $s = strval($n);
        $str.=getNumberAsText($s[0])." hundred";
        $rest = $n % (int)($s[0]."00");
        if($rest)
            $str.=" and ".getNumberAsText($rest);
    }else{
        $str = "one thousand";
    }
    
    return $str;
}

$count = 0;
$str = "";

for($i = 1; $i <= 1000; $i++){
    $s=getNumberAsText($i);
    $str.=$s;
}

echo strlen($str)."\r\n";

$str = str_replace(" ", "", $str);
$str = str_replace("-", "", $str);

echo strlen($str);