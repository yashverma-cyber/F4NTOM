import hashlib

def str_xor(secret, key):
    new_key = key
    i = 0

    while len(new_key) < len(secret):
        new_key += key[i]
        i = (i + 1) % len(key)

    return "".join(
        chr(ord(secret_c) ^ ord(new_key_c))
        for secret_c, new_key_c in zip(secret, new_key)
    )


# Read the encrypted flag and target MD5 hash
with open("level5.flag.txt.enc", "rb") as f:
    flag_enc = f.read()

with open("level5.hash.bin", "rb") as f:
    correct_pw_hash = f.read()


# Try every 4-digit hexadecimal password: 0001 -> ffff
for i in range(1, 0x10000):

    password = f"{i:04x}"

    # Calculate MD5 of the candidate password
    password_hash = hashlib.md5(password.encode()).digest()

    # Check whether it matches the stored hash
    if password_hash == correct_pw_hash:

        print("[+] Password found:", password)

        # Decrypt the flag
        flag = str_xor(flag_enc.decode(), password)

        print("[+] Flag:", flag)
        break

else:
    print("[-] Password not found")
