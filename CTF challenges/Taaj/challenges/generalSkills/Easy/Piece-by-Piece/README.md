# picoCTF — Piece by Piece

> **Category:** General Skills / Linux
> **Challenge:** Piece by Piece
> **Platform:** picoCTF

## Challenge Description

> After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag.
>
> SSH to `dolphin-cove.picoctf.net:59635` and login as `ctf-player`.
>
> **Password:** `8d076785`

---

## 1. SSH into the Server

The challenge provides SSH access.

Connect using:

```bash
ssh ctf-player@dolphin-cove.picoctf.net -p 59635
```

When prompted for the password, enter:

```text
8d076785
```

After logging in, we can inspect the home directory:

```bash
ls
```

The output is:

```text
instructions.txt
part_aa
part_ab
part_ac
part_ad
part_ae
```

There are five separate parts of what appears to be a file.

---

## 2. Read the Instructions

The provided `instructions.txt` explains what we need to do:

```bash
cat instructions.txt
```

Output:

```text
Hint:

- The flag is split into multiple parts as a zipped file.
- Use Linux commands to combine the parts into one file.
- The zip file is password protected. Use this "supersecret" password to extract the zip file.
- After unzipping, check the extracted text file for the flag.
```

This gives us the entire intended attack path:

```text
Split ZIP files
      ↓
Combine the parts
      ↓
Extract ZIP
      ↓
Password: supersecret
      ↓
Read flag.txt
```

---

## 3. Identify the File Type

Before combining the files, I checked one of the parts:

```bash
file part_aa
```

The output was:

```text
part_aa: Zip archive data, at least v1.0 to extract
```

This confirms that the pieces belong to a ZIP archive.

The files are named sequentially:

```text
part_aa
part_ab
part_ac
part_ad
part_ae
```

So they need to be concatenated in that order.

---

## 4. Combine the File Parts

Linux's `cat` command can concatenate multiple files.

I combined all five parts into a single ZIP file:

```bash
cat part_aa part_ab part_ac part_ad part_ae > flag.zip
```

This creates:

```text
flag.zip
```

containing the complete ZIP archive.

---

## 5. Extract the ZIP

The instructions tell us that the ZIP is password protected and provide the password:

```text
supersecret
```

Extract it using:

```bash
unzip -P supersecret flag.zip
```

The output was:

```text
Archive:  flag.zip
 extracting: flag.txt
```

The extracted file is:

```text
flag.txt
```

---

## 6. Read the Flag

Finally:

```bash
cat flag.txt
```

The flag is:

```text
picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_4e5c49a8}
```

---

## Complete Solution

### Connect to the server

```bash
ssh ctf-player@dolphin-cove.picoctf.net -p 59635
```

Password:

```text
8d076785
```

### List the files

```bash
ls
```

### Read the instructions

```bash
cat instructions.txt
```

### Check the file type

```bash
file part_aa
```

### Combine the parts

```bash
cat part_aa part_ab part_ac part_ad part_ae > flag.zip
```

### Extract the ZIP

```bash
unzip -P supersecret flag.zip
```

### Read the flag

```bash
cat flag.txt
```

---

## Why It Works

The challenge splits a ZIP archive into five sequential pieces:

```text
part_aa
part_ab
part_ac
part_ad
part_ae
```

Each file is only a fragment of the original archive.

The shell redirection operator:

```text
>
```

writes the output into a new file, while `cat` combines the contents:

```bash
cat part_aa part_ab part_ac part_ad part_ae > flag.zip
```

The resulting `flag.zip` is then a valid ZIP archive.

Because it is password protected, we use the supplied password:

```bash
unzip -P supersecret flag.zip
```

This extracts `flag.txt`, which contains the flag.

---

## Key Takeaway

This challenge demonstrates a useful Linux technique: **concatenating split files with `cat`**.

The important command is:

```bash
cat part_aa part_ab part_ac part_ad part_ae > flag.zip
```

When file fragments are split sequentially, putting them back together in the correct order can reconstruct the original file.

### Flag

🏁 **`picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_4e5c49a8}`**
