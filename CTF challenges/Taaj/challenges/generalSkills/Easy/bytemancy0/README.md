# picoCTF — BYTEMANCY-0

> **Category:** General Skills / Programming
> **Challenge:** BYTEMANCY-0
> **Platform:** picoCTF

## Challenge Description

> **Can you conjure the right bytes?**
>
> The program's source code can be downloaded here:
>
> [Challenge Source Code](https://challenge-files.picoctf.net/c_candy_mountain/a9a4e646c897877b5a5aa42794c8ef7dc68015c8fc632f7e2508d557b53d644f/app.py)
>
> Connect to the program with netcat:
>
> ```bash
> nc candy-mountain.picoctf.net 52876
> ```

---

## 1. Analyze the Source Code

After downloading and inspecting `app.py`, I found the following condition:

```python
if user_input == "\x65\x65\x65":
```

The `\x` notation represents hexadecimal byte values.

Here:

```text
\x65 = hexadecimal 65
```

Converting hexadecimal `65` to decimal:

```text
0x65 = 101
```

Therefore:

```text
\x65\x65\x65
```

represents three bytes:

```text
101 101 101
```

---

## 2. Understanding the Character Representation

I initially checked what the hexadecimal escape sequence represents in Python:

```python
print("\x65\x65\x65")
```

Output:

```text
eee
```

So:

```text
\x65\x65\x65
```

is equivalent to:

```text
eee
```

However, there is an important distinction.

The challenge server does **not** ask us to send the characters `eee`.

---

## 3. Connect to the Server

Connect using netcat:

```bash
nc candy-mountain.picoctf.net 52876
```

The server displays:

```text
⊹──────[ BYTEMANCY-0 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==>
```

The crucial instruction is:

```text
Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.
```

We need to send the decimal values directly:

```text
101101101
```

There are no spaces between them.

---

## 4. Send the Correct Bytes

Enter:

```text
101101101
```

The server accepts the input and returns:

```text
picoCTF{pr1n74813_ch4r5_c7b200ac}
```

---

## 5. Flag

```text
picoCTF{pr1n74813_ch4r5_c7b200ac}
```

---

## Explanation

The trick is understanding the difference between **hexadecimal escape sequences** and **ASCII decimal representations**.

The source code contains:

```python
"\x65\x65\x65"
```

Each `\x65` represents the hexadecimal byte:

```text
0x65
```

Converting it to decimal:

```text
0x65 = 101
```

So the three bytes are:

```text
101 101 101
```

The Python representation:

```python
print("\x65\x65\x65")
```

produces:

```text
eee
```

because ASCII decimal `101` corresponds to the character `e`.

However, the challenge specifically tells us to provide the **ASCII decimal values**, side-by-side, with no spaces.

Therefore:

```text
101 + 101 + 101
```

becomes:

```text
101101101
```

### Important distinction

```text
\x65\x65\x65
      ↓
  0x65 0x65 0x65
      ↓
  101 101 101
      ↓
  101101101
      ↓
      eee
```

The challenge expects the **decimal representation**:

```text
101101101
```

not the resulting characters:

```text
eee
```

---

## Solution

```bash
nc candy-mountain.picoctf.net 52876
```

Then enter:

```text
101101101
```

### Flag

🏁 **`picoCTF{pr1n74813_ch4r5_c7b200ac}`**

---

## Takeaway

This challenge tests your ability to move between different representations of bytes:

* `\x65` → hexadecimal representation
* `0x65` → hexadecimal byte value
* `101` → decimal ASCII value
* `e` → ASCII character

The important lesson is to carefully follow the **format requested by the program**, rather than simply entering the character representation you discover from the source code.
