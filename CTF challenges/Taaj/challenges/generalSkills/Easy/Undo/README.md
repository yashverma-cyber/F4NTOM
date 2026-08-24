# Undo

> Can you reverse a series of Linux text transformations to recover the original flag?

**Category:** General Skills
**Difficulty:** Easy
**Challenge Type:** Linux / Text Transformation

---

## 📌 Challenge

The challenge provides a network service:

```bash
nc foggy-cliff.picoctf.net 60716
```

After connecting, the server gives a transformed flag and a hint at each step.

The objective is to determine the **Linux command that reverses each transformation**.

---

## 🔎 Step 1 — Base64

### Given

```text
KTJxNW85NjQ1LWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShTR1BicHZj
```

### Hint

> Base64 encoded the string.

To decode Base64:

```bash
base64 -d
```

The server accepts the command:

```text
base64 -d
```

### Result

```text
)2q5o9645-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
```

---

## 🔄 Step 2 — Reverse the Text

### Given

```text
)2q5o9645-fa01g@ze0sfa4eG-gk3g-ta1ferirE(SGPbpvc
```

### Hint

> Reversed the text.

Linux provides the `rev` command for reversing characters:

```bash
rev
```

### Result

```text
cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-5469o5q2)
```

---

## 🔤 Step 3 — Dashes to Underscores

### Given

```text
cvpbPGS(Eriref1at-g3kg-Ge4afs0ez@g10af-5469o5q2)
```

### Hint

> Replaced underscores with dashes.

The transformation replaced `_` with `-`.

To reverse it, replace `-` with `_`:

```bash
tr '-' '_'
```

### Result

```text
cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_5469o5q2)
```

---

## 🔣 Step 4 — Parentheses to Curly Braces

### Given

```text
cvpbPGS(Eriref1at_g3kg_Ge4afs0ez@g10af_5469o5q2)
```

### Hint

> Replaced curly braces with parentheses.

The original flag format uses:

```text
picoCTF{...}
```

Since `{` and `}` were replaced with `(` and `)`, reverse the transformation:

```bash
tr '()' '{}'
```

### Result

```text
cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_5469o5q2}
```

---

## 🔐 Step 5 — ROT13

### Given

```text
cvpbPGS{Eriref1at_g3kg_Ge4afs0ez@g10af_5469o5q2}
```

### Hint

> Applied ROT13 to letters.

ROT13 is its own inverse, meaning applying ROT13 again reverses the transformation.

Use:

```bash
tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

### Result

```text
picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_5469b5d2}
```

---

# 🚩 Flag

```text
picoCTF{Revers1ng_t3xt_Tr4nsf0rm@t10ns_5469b5d2}
```

---

# 🧠 Solution Summary

The important concept is that transformations must be reversed in the **opposite order** in which they were originally applied.

| Step | Transformation  | Reverse Command              |
| ---- | --------------- | ---------------------------- |
| 1    | Base64 encoding | `base64 -d`                  |
| 2    | Text reversal   | `rev`                        |
| 3    | `_` → `-`       | `tr '-' '_'`                 |
| 4    | `{}` → `()`     | `tr '()' '{}'`               |
| 5    | ROT13           | `tr 'A-Za-z' 'N-ZA-Mn-za-m'` |

The complete reverse process is therefore:

```bash
base64 -d
```

```bash
rev
```

```bash
tr '-' '_'
```

```bash
tr '()' '{}'
```

```bash
tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

---

# 💡 Key Takeaways

* `base64 -d` decodes Base64 data.
* `rev` reverses the order of characters in a line.
* `tr` can replace one set of characters with another.
* ROT13 is reversible by applying the same transformation again.
* When reversing a sequence of transformations, work **backwards from the final output**.
* The Linux command line is extremely useful for manipulating and analyzing text during CTFs.

---

# 🛠️ Skills Practiced

```text
Linux command line
Base64 decoding
Text manipulation
Character substitution
ROT13
Reverse transformations
CTF methodology
```

> **Lesson:** When a challenge gives you a sequence of transformations, don't try to guess the final flag immediately. Identify the last transformation and systematically undo each operation until the original data is recovered.
