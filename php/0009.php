<?php

for($a = 1;$a < 1000; $a++){
	for($b = 1;$b < 1000; $b++){
		for($c = 1;$c < 1000; $c++){
			if($a + $b + $c === 1000 && pow($a,2) + pow($b,2) === pow($c,2)){
                $p = $a*$b*$c;
				echo "$a + $b + $c = $p";
				return;
			}
		}
	}	
}

