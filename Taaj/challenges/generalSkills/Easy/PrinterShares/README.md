Printer Shares

Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?

The printer is on 52347.

you can try $ nc -vz mysterious-sea.picoctf.net 52347


i tried to connect but it says 

nc -vz mysterious-sea.picoctf.net 52347
DNS fwd/rev mismatch: mysterious-sea.picoctf.net != ec2-3-130-79-223.us-east-2.compute.amazonaws.com
mysterious-sea.picoctf.net [3.130.79.223] 52347 (?) open


this give mysterious-sea.picoctf.net [3.130.79.223] 52347 (?) open

and in hint it says abt smbclient

so lets try



smbclient -L //mysterious-sea.picoctf.net -p 52347 --no-pass

        Sharename       Type      Comment
        ---------       ----      -------
        shares          Disk      Public Share With Guests
        IPC$            IPC       IPC Service (Samba 4.19.5-Ubuntu)
Reconnecting with SMB1 for workgroup listing.
do_connect: Connection to mysterious-sea.picoctf.net failed (Error NT_STATUS_CONNECTION_REFUSED)
Unable to connect with SMB1 -- no workgroup available

and here that shares seems interesting so lets try to access that

smbclient //mysterious-sea.picoctf.net/shares -p 52347 --no-pass
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Fri Mar  6 15:25:40 2026
  ..                                  D        0  Fri Mar  6 15:25:40 2026
  dummy.txt                           N     1142  Wed Feb  4 16:22:17 2026
  flag.txt                            N       37  Fri Mar  6 15:25:40 2026

                65536 blocks of size 1024. 58680 blocks available
smb: \> cat flag.txt
cat: command not found
smb: \> get flag.txt
getting file \flag.txt of size 37 as flag.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \> ^C
                                                                                                                                           
┌──(taaj㉿kali)-[PrinterShares]
└─$ cat flag.txt   
picoCTF{5mb_pr1nter_5h4re5_ac4c227e}

# picoCTF — Printer Shares

> **Category:** General Skills / Network
> **Challenge:** Printer Shares
> **Platform:** picoCTF

## Challenge Description

> Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server?
>
> The printer is on port `52347`.

---

## 1. Check the Port

The challenge gives us a host and port:

```text
mysterious-sea.picoctf.net:52347
```

First, I checked whether the port was accessible:

```bash
nc -vz mysterious-sea.picoctf.net 52347
```

The result was:

```text
DNS fwd/rev mismatch: mysterious-sea.picoctf.net != ec2-3-130-79-223.us-east-2.compute.amazonaws.com
mysterious-sea.picoctf.net [3.130.79.223] 52347 (?) open
```

The important part is:

```text
52347 (?) open
```

So the port is reachable.

The DNS forward/reverse mismatch is not important for solving the challenge.

---

## 2. SMB Enumeration

The hint mentions `smbclient`, so I used it to enumerate the available SMB shares:

```bash
smbclient -L //mysterious-sea.picoctf.net -p 52347 --no-pass
```

The server returned:

```text
Sharename       Type      Comment
---------       ----      -------
shares          Disk      Public Share With Guests
IPC$            IPC       IPC Service (Samba 4.19.5-Ubuntu)
```

The interesting share is:

```text
shares
```

because its comment says:

```text
Public Share With Guests
```

This indicates that we may be able to access it without credentials.

---

## 3. Connect to the `shares` Share

I connected to the share using guest access:

```bash
smbclient //mysterious-sea.picoctf.net/shares -p 52347 --no-pass
```

This opened an interactive SMB shell:

```text
Try "help" to get a list of possible commands.
smb: \>
```

---

## 4. List the Files

Inside the SMB shell, I listed the contents:

```text
smb: \> ls
```

The server returned:

```text
.                                   D        0  Fri Mar  6 15:25:40 2026
..                                  D        0  Fri Mar  6 15:25:40 2026
dummy.txt                           N     1142  Wed Feb  4 16:22:17 2026
flag.txt                            N       37  Fri Mar  6 15:25:40 2026
```

There are two files:

```text
dummy.txt
flag.txt
```

Obviously, `flag.txt` is the file we're looking for.

---

## 5. Download the Flag

I initially tried:

```text
smb: \> cat flag.txt
```

but `cat` is a local shell command and isn't available inside the `smbclient` prompt:

```text
cat: command not found
```

Instead, SMB provides the `get` command to download a file.

```text
smb: \> get flag.txt
```

The server responded:

```text
getting file \flag.txt of size 37 as flag.txt
```

The file was downloaded to my local directory.

Exit `smbclient`:

```text
smb: \> exit
```

Then read the downloaded file:

```bash
cat flag.txt
```

Output:

```text
picoCTF{5mb_pr1nter_5h4re5_ac4c227e}
```

---

## 6. Flag

```text
picoCTF{5mb_pr1nter_5h4re5_ac4c227e}
```

---

## Complete Solution

### Check the port

```bash
nc -vz mysterious-sea.picoctf.net 52347
```

### Enumerate SMB shares

```bash
smbclient -L //mysterious-sea.picoctf.net -p 52347 --no-pass
```

### Connect to the public share

```bash
smbclient //mysterious-sea.picoctf.net/shares -p 52347 --no-pass
```

### List files

```text
ls
```

### Download the flag

```text
get flag.txt
```

### Exit and read it locally

```text
exit
```

```bash
cat flag.txt
```

---

## Key Takeaway

The challenge was about identifying the service running on the unusual port.

The workflow was:

```text
Open port
   ↓
SMB service
   ↓
Enumerate shares
   ↓
Public guest-accessible share
   ↓
Find flag.txt
   ↓
Download with get
   ↓
Read flag
```

The `--no-pass` option allowed us to attempt anonymous/guest access without providing credentials.

Also, remember that `smbclient` has its own command set. To download a remote file, use:

```text
get <filename>
```

rather than trying to use local shell commands such as `cat`.

### Flag

🏁 **`picoCTF{5mb_pr1nter_5h4re5_ac4c227e}`**
