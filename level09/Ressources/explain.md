# Start / Search


```sh
level09@SnowCrash:~$ ls -la
[...]
-rwsr-sr-x 1 flag09  level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09  level09   26 Mar  5  2016 token
```
>> level09 thaat  we can read and execute | toke that we can read

```sh
level09@SnowCrash:~$ cat token 
f4kmm6p|=�p�n��DB�Du{��
```

```sh
level09@SnowCrash:~$ ./level09 `cat token`
f5mpq;v�E��{�{��TS�W�����
```
>> it modify the string pass in parameter

```sh
level09@SnowCrash:~$ ./level09 aaa
abc
```
>> it's n to each n letter

# Resolve

level09 try to decode by adding the index to the char, we try the opposite
>> see script.py

```sh
level09@SnowCrash:~$ vim /tmp/script.py
level09@SnowCrash:~$ python /tmp/script.py `cat token`
f3iji1ju5yuevaus41q1afiuq
```
>> f3iji1ju5yuevaus41q1afiuq is the password of flag09


