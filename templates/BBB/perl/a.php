<?php


$cmd = "python 1.py";
exec($cmd, $out);
echo $out[0];
echo $out[1];


?>
