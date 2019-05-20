<?php 
function a($q, $y, $z, $p, $e, $k)
{
    return ($z >> 5 & 134217727 ^ $y << 2) + ($y >> 3 & 536870911 ^ $z << 4) ^ ($q ^ $y) + ($k[$p & 3 ^ $e] ^ $z);
}

function verify($str)
{
    if( php_sapi_name() === "phpdbg" ) 
    {
        exit( "Sorry but no phpdbg" );
    }

    if( ini_get("vld.active") == 1 ) 
    {
        dir("Sorry but no vld");
    }

    $v = unpack("V*", $str . str_repeat("", 4 - strlen($str) % 4 & 3));
    $v = array_values($v);
    $v[count($v)] = strlen($str);
    $b = array( 1029560848, 2323109303, 4208702724, 3423862500, 3597800709, 2222997091, 4137082249, 2050017171, 4045896598 );
    $k = array( 1752186684, 1600069744, 1953259880, 1836016479 );
    $n = count($v) - 1;
    $z = $v[$n];
    $q = floor(6 + 52 / ($n + 1));
    $sum = 0;
    while( 0 < $q-- ) 
    {
        $sum = $sum + 2654435769 & 4294967295;
        $e = $sum >> 2 & 3;
        $p = 0;
        while( $p < $n ) 
        {
            $y = $v[$p + 1];
            $v[$p] = $v[$p] + a($sum, $y, $z, $p, $e, $k) & 4294967295;
            $z = $v[$p];
            $p++;
        }
        $y = $v[0];
        $v[$n] = $v[$n] + a($sum, $y, $z, $p, $e, $k) & 4294967295;
        $z = $v[$n];
    }
    $i = 0;
    while( $i < count($v) ) 
    {
        $v[$i] = $v[$i] ^ $k[$i % 4];
        $i++;
    }
    return $v == $b;
}


