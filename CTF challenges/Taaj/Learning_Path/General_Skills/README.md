# 🏴 picoCTF — General Skills in CTF's

A collection of my solutions to beginner-level challenges from **picoCTF**.

This README documents the approach, commands, and reasoning used to solve each challenge. The goal is not just to record the flags, but also to document the techniques and tools used along the way.

---

## 📌 Challenges

| # | Challenge                     | Category       | Technique                 |
| - | ----------------------------- | -------------- | ------------------------- |
| 1 | **Lets Warm Up**              | General Skills | Hex → ASCII               |
| 2 | **convertme.py**              | General Skills | Decimal → Binary          |
| 3 | **Nice netcat...**            | General Skills | Netcat + Bash             |
| 4 | **Magikarp Ground Mission**   | General Skills | SSH + Linux Navigation    |
| 5 | **First Find**                | General Skills | `grep` + Recursive Search |
| 6 | **Static ain't always noise** | General Skills | Binary Analysis + Strings |
| 7 | **plumbing**                  | General Skills | Pipes + `grep`            |

---

# 1. 🔥 Lets Warm Up

## 📝 Challenge

> If I told you a word started with `0x70` in hexadecimal, what would it start with in ASCII?

## 💡 Approach

After reading the question, I went straight to **CyberChef**.

I used the **From Hex** operation:

```text
Input:
0x70

Output:
p
```

Therefore:

## 🚩 Flag

```text
picoCTF{p}
```

## 🔑 Takeaway

A quick introduction to converting hexadecimal values into ASCII characters.

---

# 2. 🐍 convertme.py

## 📝 Challenge

> Run the Python script and convert the given number from decimal to binary to get the flag.

After downloading `convertme.py`, I ran:

```bash
python convertme.py
```

The script asked:

```text
If 91 is in decimal base, what is it in binary base?

Input:
```

## 💡 Approach

The task was simply to convert decimal `91` into binary.

I used CyberChef with:

```text
From Decimal
↓
To Binary
```

The correct conversion is:

```text
91 (decimal) = 1011011 (binary)
```

I entered the answer into the script:

```bash
python convertme.py
```

```text
If 91 is in decimal base, what is it in binary base?
Answer: 1011011

That is correct! Here's your flag:
```

## 🚩 Flag

The final flag was displayed by the script.

> **Note:** The actual flag was not included in my original notes, so it is intentionally not guessed here.

## 🔑 Takeaway

Binary conversion is a common basic skill in CTFs.

Python can also perform the conversion directly:

```python
bin(91)
```

Output:

```text
0b1011011
```

---

# 3. 🐱 Nice netcat...

## 📝 Challenge

> There is a nice program that you can talk to by using this command in a shell:
>
> `nc wily-courier.picoctf.net 56418`
>
> but it doesn't speak English...

## 💡 Approach

I connected to the service using Netcat:

```bash
nc wily-courier.picoctf.net 56418
```

The service printed a bunch of numbers instead of readable text.

The numbers appeared to be decimal ASCII character codes.

Instead of converting them manually, I wrote a small Bash script named `shell.sh` to automatically convert each number into a character.

### `shell.sh`

```bash
#!/bin/bash

HOST="wily-courier.picoctf.net"
PORT="56418"

nc "$HOST" "$PORT" | while read -r decimal; do
    printf "\\$(printf '%03o' "$decimal")"
done

printf '\n'
```

I then gave the script execute permissions:

```bash
chmod +x shell.sh
```

And ran it:

```bash
./shell.sh
```

The script converted the incoming decimal values into readable ASCII and revealed the flag.

## 🚩 Flag

```text
picoCTF{g00d_k1tty!_n1c3_k1tty!_d9476}
```

## 🔑 Takeaway

This challenge was a good introduction to:

* `nc` / Netcat
* Bash scripting
* Pipes
* Reading data line-by-line
* Converting character codes into ASCII

---

# 4. 🐟 Magikarp Ground Mission

## 📝 Challenge

> Do you know how to move between directories and read files in the shell? Start the container, ssh to it, and then ls once connected to begin.

The challenge provided SSH credentials:

```text
Username: ctf-player
Password: 8c606eb1
Host: wily-courier.picoctf.net
Port: 62315
```

## 🔌 Step 1 — SSH

I connected to the challenge machine using:

```bash
ssh ctf-player@wily-courier.picoctf.net -p 62315
```

After logging in:

```bash
ctf-player@pico-chall$ ls
```

Output:

```text
1of3.flag.txt
instructions-to-2of3.txt
```

## 🚩 Step 2 — First Flag Fragment

I read the first flag file:

```bash
ctf-player@pico-chall$ cat 1of3.flag.txt
```

Output:

```text
picoCTF{xxsh_
```

The instructions then told me:

```text
Next, go to the root of all things, more succinctly `/`
```

## 🚩 Step 3 — Second Flag Fragment

I followed the instruction:

```bash
ctf-player@pico-chall$ cd /
```

Then:

```bash
ctf-player@pico-chall$ ls
```

Among the files was:

```text
2of3.flag.txt
instructions-to-3of3.txt
```

I read the second fragment:

```bash
ctf-player@pico-chall$ cat 2of3.flag.txt
```

Output:

```text
0ut_0f_//4t3r_
```

The next instruction said:

```text
Lastly, ctf-player, go home... more succinctly `~`
```

## 🚩 Step 4 — Third Flag Fragment

I followed the instruction and went to the home directory:

```bash
ctf-player@pico-chall$ cd /home/ctf-player/
```

Then:

```bash
ctf-player@pico-chall$ ls
```

Output:

```text
3of3.flag.txt
drop-in
```

I read the final fragment:

```bash
ctf-player@pico-chall$ cat 3of3.flag.txt
```

Output:

```text
0b24fc4f}
```

## 🧩 Step 5 — Assemble the Flag

The three pieces were:

```text
picoCTF{xxsh_
0ut_0f_//4t3r_
0b24fc4f}
```

Combining them:

## 🚩 Flag

```text
picoCTF{xxsh_0ut_0f_//4t3r_0b24fc4f}
```

## 🔑 Takeaway

This challenge reinforced some essential Linux commands:

```bash
ls
cd
cat
```

It also introduced basic SSH usage.

---

# 5. 🔎 First Find

## 📝 Challenge

> Unzip this archive and find the file named `uber-secret.txt`

After downloading the archive, I extracted it with:

```bash
unzip files.zip
```

I then inspected the directory structure:

```bash
tree
```

The archive contained multiple nested directories and files:

```text
.
├── files
│   ├── 13771.txt.utf-8
│   ├── 14789.txt.utf-8
│   ├── acceptable_books
│   │   ├── 17879.txt.utf-8
│   │   ├── 17880.txt.utf-8
│   │   └── more_books
│   │       └── 40723.txt.utf-8
│   ├── adequate_books
│   │   ├── 44578.txt.utf-8
│   │   ├── 46804-0.txt
│   │   └── more_books
│   │       └── 1023.txt.utf-8
│   └── satisfactory_books
│       ├── 16021.txt.utf-8
│       ├── 23765.txt.utf-8
│       └── more_books
│           └── 37121.txt.utf-8
└── files.zip
```

## 💡 Approach

Instead of manually checking every directory, I used recursive `grep` to search for the string `pico`:

```bash
grep -r "pico" ./files
```

The search returned:

```text
./files/adequate_books/more_books/.secret/deeper_secrets/deepest_secrets/uber-secret.txt:picoCTF{f1nd_15_f457_ab443fd1}
```

This immediately revealed both the location of `uber-secret.txt` and the flag.

## 🚩 Flag

```text
picoCTF{f1nd_15_f457_ab443fd1}
```

## 🔑 Takeaway

Recursive searching is extremely useful when dealing with large directory structures.

A useful command to remember:

```bash
grep -r "keyword" directory/
```

---

# 6. ⚙️ Static ain't always noise

## 📝 Challenge

> Can you look at the data in this binary? The bash script might help!

## 📦 Files

The challenge provided:

```text
static
ltdis.sh
```

## 💡 Step 1 — Make the Script Executable

I first gave `ltdis.sh` execute permissions:

```bash
chmod +x ltdis.sh
```

Running it without any arguments:

```bash
./ltdis.sh
```

produced:

```text
Attempting disassembly of  ...
objdump: 'a.out': No such file
objdump: section '.text' mentioned in a -j option, but not found in any input file
Disassembly failed!
Usage: ltdis.sh <program-file>
Bye!
```

The important part was:

```text
Usage: ltdis.sh <program-file>
```

So the script expected the binary as an argument.

## 💡 Step 2 — Analyze the Binary

I ran:

```bash
./ltdis.sh static
```

This time the script successfully processed the binary:

```text
Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset
```

The script generated:

```text
static.ltdis.x86_64.txt
static.ltdis.strings.txt
```

## 💡 Step 3 — Search the Extracted Strings

Instead of manually reading the entire strings file, I searched for `pico`:

```bash
cat static.ltdis.strings.txt | grep pico
```

The result:

```text
3020 picoCTF{d15a5m_t34s3r_20335e41}
```

## 🚩 Flag

```text
picoCTF{d15a5m_t34s3r_20335e41}
```

## 🔑 Takeaway

This challenge introduced a simple binary-analysis workflow:

```text
Binary
   │
   ▼
Disassemble
   │
   ▼
Extract Strings
   │
   ▼
Search for Interesting Data
   │
   ▼
Flag
```

Useful tools and commands:

```bash
objdump
strings
grep
```

---

# 7. 🚰 plumbing

## 📝 Challenge

> Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag?

After launching the challenge instance, I was given:

```text
fickle-tempest.picoctf.net:64476
```

## 💡 Approach

I first connected to the service using Netcat:

```bash
nc fickle-tempest.picoctf.net 64476
```

The service returned a large amount of output that wasn't immediately useful.

Instead of manually reading everything, I piped the output directly into `grep` and searched for `pico`:

```bash
nc fickle-tempest.picoctf.net 64476 | grep pico
```

The flag appeared immediately:

```text
picoCTF{digital_plumb3r_11fffFE5}
```

## 🚩 Flag

```text
picoCTF{digital_plumb3r_11fffFE5}
```

## 🔑 Takeaway

This challenge is a great example of Unix pipes:

```text
Command A | Command B
```

The output of the first command becomes the input of the second command.

In this case:

```bash
nc fickle-tempest.picoctf.net 64476 | grep pico
```

The workflow is:

```text
        Netcat
           │
           ▼
    Large amount of data
           │
           ▼
         grep
           │
           ▼
       Flag found
```

---

# 🧠 What I Learned

These challenges covered several fundamental CTF and Linux skills:

| Skill               | Example                        |
| ------------------- | ------------------------------ |
| Hexadecimal → ASCII | `0x70 → p`                     |
| Decimal → Binary    | `91 → 1011011`                 |
| SSH                 | `ssh user@host -p PORT`        |
| Linux navigation    | `cd`, `ls`, `cat`              |
| Recursive searching | `grep -r`                      |
| Pipes               | `command1 \| command2`         |
| Network interaction | `nc`                           |
| Bash scripting      | Automated character conversion |
| Binary analysis     | `objdump`, extracted strings   |
| File discovery      | `tree`, recursive search       |

---

# 🛠️ Tools Used

| Tool                 | Purpose                           |
| -------------------- | --------------------------------- |
| 🐧 **Linux / Bash**  | General environment and scripting |
| 🔌 **Netcat (`nc`)** | Connecting to remote services     |
| 🐍 **Python**        | Running challenge scripts         |
| 🔎 **grep**          | Searching through output/files    |
| 📂 **tree**          | Inspecting directory structures   |
| 📦 **unzip**         | Extracting challenge archives     |
| ⚙️ **objdump**       | Binary disassembly                |
| 📝 **strings**       | Extracting readable strings       |
| 🍳 **CyberChef**     | Data/encoding conversions         |
| 🔐 **SSH**           | Remote shell access               |

---

# 🎯 Key Lessons

### 1. Automate repetitive work

If a service gives you hundreds of numbers, don't manually decode them.

Write a script.

```bash
nc host port | ./decoder.sh
```

---

### 2. Learn your Linux basics

Commands like:

```bash
ls
cd
cat
grep
chmod
```

may look simple, but they are incredibly powerful during CTFs.

---

### 3. Pipes are powerful

Instead of saving output to a file and manually searching it:

```bash
nc host port | grep pico
```

You can process data as it flows.

---

### 4. Search before exploring manually

When a directory contains many files:

```bash
grep -r "pico" ./files
```

can be much faster than opening everything individually.

---

### 5. Understand the tools you're given

When `ltdis.sh` failed initially, the error message told me exactly what was wrong:

```text
Usage: ltdis.sh <program-file>
```

Reading error messages carefully is an important CTF skill.

---

# 🏁 Final Thoughts

These challenges were a great introduction to the mindset required for CTFs.

The biggest lesson was:

> **Don't do manually what you can automate.**

Whether it was converting character codes, searching through nested directories, analyzing a binary, or filtering noisy network output, the key was recognizing the pattern and choosing the right tool.

The more I work through these challenges, the more obvious it becomes that **strong Linux fundamentals are extremely useful in CTFs**.

Knowing how to manipulate files, pipe commands together, search recursively, write small scripts, and interact with remote services can turn seemingly complicated problems into simple ones.

---


### 🏴 Happy Hacking & Keep Learning! 🚩

