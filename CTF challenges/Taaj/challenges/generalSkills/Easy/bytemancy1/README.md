# picoCTF — BYTEMANCY-1

> **Category:** General Skills / Programming
> **Challenge:** BYTEMANCY-1
> **Platform:** picoCTF

## Challenge Description

> **Can you conjure the right bytes?**
>
> The program's source code can be downloaded here:
>
> [Challenge Source Code](https://challenge-files.picoctf.net/c_foggy_cliff/51942c7b5e398fe37f39beef2365716ac6cf1d68fba0b9cf7c7035dee3f302f3/app.py)
>
> Connect to the program with netcat:
>
> ```bash
> nc foggy-cliff.picoctf.net 51822
> ```

---

## 1. Analyze the Source Code

After inspecting `app.py`, I found:

```python
if user_input == "\x65"*1751:
```

The important part is:

```text
\x65
```

As in the previous BYTEMANCY challenge:

```text
0x65 = 101
```

and ASCII decimal `101` represents the character:

```text
e
```

The `*1751` means that this byte must be repeated **1,751 times**.

Therefore, the expected value is:

```text
\x65\x65\x65\x65... 
```

with `\x65` appearing 1,751 times.

---

## 2. Understand What the Server Wants

After connecting to the server:

```bash
nc foggy-cliff.picoctf.net 51822
```

the challenge displays:

```text
⊹──────[ BYTEMANCY-1 ]──────⊹

Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.
```

The key instruction is:

> **Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.**

So we need to provide:

```text
101101101101101...
```

with `101` repeated exactly **1,751 times**.

This time, simply entering `e` 1,751 times would not satisfy the server's requested format.

---

## 3. Generate the Correct Input

Rather than manually typing 1,751 repetitions, Python can generate the required string:

```python
print("101" * 1751)
```

This produces `101` repeated 1,751 times with no spaces.

The equivalent character representation is:

```python
print("\x65" * 1751)
```

which produces:

```text
eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee...
```

But the server specifically requests the **ASCII decimal representation**, so the correct input is:

```text
101101101101101...
```

---

## 4. Connect to the Server

Run:

```bash
nc foggy-cliff.picoctf.net 51822
```

The server responds with:

```text
⊹──────[ BYTEMANCY-1 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==>
```

Generate the answer with:

```python
print("101" * 1751)
```

Then paste the generated string into the server.

The server accepts the input and returns:

```text
picoCTF{h0w_m4ny_e's???_0c1ad83a}
```

---

## 5. Why It Works

The source code:

```python
if user_input == "\x65"*1751:
```

can be broken down into:

```text
\x65
```

↓

```text
0x65
```

↓

```text
101
```

↓

```text
e
```

The multiplication operator means:

```text
\x65 * 1751
```

so the program expects the byte represented by `0x65` exactly **1,751 times**.

The challenge converts that requirement into its decimal representation:

```text
101 101 101 101 ...
```

and tells us to remove the spaces:

```text
101101101101101...
```

So the transformation is:

```text
\x65 * 1751
        ↓
ASCII character: e * 1751
        ↓
ASCII decimal: 101 * 1751
        ↓
101101101101101...
```

---

## 6. Flag

```text
picoCTF{h0w_m4ny_e's???_0c1ad83a}
```

---

## Quick Solution

The important source-code line was:

```python
if user_input == "\x65"*1751:
```

The server asks for ASCII decimal `101` repeated 1,751 times.

Generate it with:

```python
print("101" * 1751)
```

Then connect:

```bash
nc foggy-cliff.picoctf.net 51822
```

Paste the generated value.

### Flag

🏁 **`picoCTF{h0w_m4ny_e's???_0c1ad83a}`**

---

## Takeaway

BYTEMANCY-1 builds directly on BYTEMANCY-0:

* `\x65` is hexadecimal.
* `0x65` equals decimal `101`.
* ASCII decimal `101` represents `e`.
* `*1751` means the byte must occur 1,751 times.
* The server wants the decimal value `101` repeated 1,751 times, **without spaces**.

The main challenge is not the conversion itself, but recognizing that the server wants the **decimal byte representation**, rather than the resulting ASCII characters.
