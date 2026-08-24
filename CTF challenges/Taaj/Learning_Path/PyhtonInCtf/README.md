# 🐍 Python in CTFs

> **Learning Path:** `Python in CTF's`

A collection of my solutions to beginner Python-based challenges from **picoCTF**.

These challenges focus on identifying and fixing common Python syntax errors. While the challenges themselves are simple, they are a good introduction to debugging Python code — an essential skill when working with CTF scripts.

---

## 📌 Challenges

| # | Challenge     | Concept     | Technique              |
| - | ------------- | ----------- | ---------------------- |
| 1 | **fixme1.py** | Indentation | Fix `IndentationError` |
| 2 | **fixme2.py** | Operators   | Fix `SyntaxError`      |

---

# 1. 🔧 fixme1.py

## 📝 Challenge

> Fix the syntax error in this Python script to print the flag.

After downloading the challenge file, I first ran the script to see what was wrong.

```bash
python fixme1.py
```

The script returned:

```text
File "/home/taaj/PicoCTF/PyhtonInCtf/fixme1/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
```

---

## 🔍 Understanding the Error

The important part of the error was:

```text
IndentationError: unexpected indent
```

Python uses indentation to define blocks of code, so an unexpected tab or space can cause the entire program to fail.

Looking at the code, the `print()` statement had an extra tab/indentation before it.

### ❌ Incorrect

```python
    print('That is correct! Here\'s your flag: ' + flag)
```

The indentation did not match the surrounding code.

### ✅ Fix

I removed the extra tab/space before the `print()` function.

After saving the corrected file, I ran it again:

```bash
python fixme1_corrected.py
```

The script successfully executed:

```text
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}
```

---

## 🚩 Flag

```text
picoCTF{1nd3nt1ty_cr1515_09ee727a}
```

---

## 🧠 What I Learned

Python is very strict about indentation.

Unlike languages that use `{}` to define code blocks, Python uses indentation to determine which statements belong together.

For example:

```python
if condition:
    print("Correct")
```

The indentation is part of the syntax itself.

A small extra tab or space can therefore result in:

```text
IndentationError
```

### 🔑 Key takeaway

> **When Python throws an `IndentationError`, check the whitespace around the affected line and the surrounding code block.**

---

# 2. ⚖️ fixme2.py

## 📝 Challenge

> Fix the syntax error in this Python script to print the flag.

After downloading the file, I ran the script:

```bash
python fixme2.py
```

Python returned:

```text
File "/home/taaj/PicoCTF/PyhtonInCtf/fixme2/fixme2.py", line 22
    if flag = "":
       ^^^^^^^^^
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

---

## 🔍 Understanding the Error

The problem was this line:

```python
if flag = "":
```

The `=` operator is used for **assignment**, while `==` is used for **comparison**.

### ❌ Incorrect

```python
if flag = "":
```

This attempts to assign an empty string to `flag` inside an `if` condition, which is invalid Python syntax.

### ✅ Correct

```python
if flag == "":
```

The `==` operator checks whether two values are equal.

I changed the line from:

```python
if flag = "":
```

to:

```python
if flag == "":
```

---

## ▶️ Running the Corrected Script

After saving the changes, I ran:

```bash
python fixme2_corrected.py
```

This time the script executed successfully:

```text
That is correct! Here's your flag: picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```

---

## 🚩 Flag

```text
picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}
```

---

## 🧠 What I Learned

One of the most important Python distinctions is between assignment and comparison.

### Assignment — `=`

Used to assign a value:

```python
flag = ""
```

### Comparison — `==`

Used to compare two values:

```python
if flag == "":
    print("Flag is empty")
```

Using `=` where `==` is required results in a syntax error.

### 🔑 Key takeaway

> **`=` assigns a value, while `==` compares values.**

This is a very common mistake when writing or debugging Python code.

---

# 🧠 Concepts Covered

These two challenges introduced a couple of fundamental Python concepts:

| Concept     | Incorrect         | Correct                |
| ----------- | ----------------- | ---------------------- |
| Indentation | Extra indentation | Consistent indentation |
| Assignment  | `flag = ""`       | `flag = ""`            |
| Comparison  | `if flag = ""`    | `if flag == ""`        |

---

# 🛠️ Useful Python Debugging Workflow

When given a Python challenge that doesn't run, I use a simple workflow:

### 1. Run the script

```bash
python script.py
```

### 2. Read the error carefully

Python usually tells you:

* The file
* The line number
* The type of error
* Sometimes even a suggested fix

### 3. Inspect the affected line

For example:

```text
IndentationError
```

→ Check indentation.

Or:

```text
SyntaxError
```

→ Check the syntax around the reported line.

### 4. Make the smallest necessary change

Avoid changing unrelated code.

### 5. Run the script again

```bash
python script.py
```

If the script executes successfully, inspect the output.

---

# 📚 Lessons Learned

## 🐍 1. Python cares about indentation

Whitespace isn't just formatting in Python — it can determine program structure.

```python
if True:
    print("Hello")
```

is valid, while inconsistent indentation can cause an error.

---

## ⚖️ 2. Know your operators

A few operators worth remembering:

```text
=    Assignment
==   Equality comparison
!=   Not equal
>    Greater than
<    Less than
>=   Greater than or equal
<=   Less than or equal
```

---

## 🔎 3. Read error messages

The Python interpreter often gives extremely useful information.

For example:

```text
IndentationError: unexpected indent
```

immediately points toward a whitespace problem.

Likewise:

```text
SyntaxError: invalid syntax
```

means the interpreter couldn't parse the code correctly.

---

# 🏁 Final Thoughts

These were simple challenges, but they demonstrate an important CTF skill:

> **Don't just look at the challenge — read what the program is telling you.**

Python's error messages often provide enough information to identify the problem without having to understand the entire program.

The two main lessons from this section were:

```text
Indentation matters.
       +
Syntax matters.
       ↓
Read the error → Fix the issue → Run again → Get the flag
```

---

## 🚩 Flags Obtained

| Challenge   | Flag                                        |
| ----------- | ------------------------------------------- |
| `fixme1.py` | `picoCTF{1nd3nt1ty_cr1515_09ee727a}`        |
| `fixme2.py` | `picoCTF{3qu4l1ty_n0t_4551gnm3nt_4863e11b}` |

---

<p align="center">

### 🐍 Keep Coding. Keep Hacking. Keep Learning. 🚩

</p>
