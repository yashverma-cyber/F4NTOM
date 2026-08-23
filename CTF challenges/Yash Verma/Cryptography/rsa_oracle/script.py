#!/usr/bin/env python3
from pwn import *
from subprocess import run, PIPE
import re
import math

# Use the active port given by your instance
p = remote("titan.picoctf.net", 54334)

with open('./password.txt') as f:
    password = f.read().strip()

# 1. Get Banner plus options menu
print(p.recvuntil(b'decrypt.').decode())
p.sendline('E'.encode())

# 2. Gets until "enter text to encrypt ... :"
p.recvuntil(b':')
ourValue = 'a'
p.sendline(ourValue.encode())

# Read all output until the menu returns
data_raw = p.recvuntil(b'decrypt.').decode()

# FIXED: Extract the huge ciphertext integer via RegEx instead of brittle split(' ')
data_match = re.search(r'mod\s+n\)?\s*(\d+)', data_raw)
if not data_match:
    log.failure("Could not parse ciphertext integer from output!")
    exit(1)

data = int(data_match.group(1))
log.info(f'data = {data}')

# Blinding calculation
toDecrypt = int(password) * data
log.info(f"Calculated payload: {toDecrypt}")

# 3. Decrypts toDecrypt
p.sendline('D'.encode())
p.recvuntil(b':') 
p.sendline(str(toDecrypt).encode())

res_raw = p.recvuntil(b'decrypt.').decode()

# FIXED: Extract the returned hex response via RegEx safely
res_match = re.search(r'mod\s+n\):\s*([0-9a-fA-F]+)', res_raw)
if not res_match:
    log.failure("Could not parse decrypted hex from output!")
    exit(1)

res = res_match.group(1)
log.info(f"Captured hex output: {res}")

# 4. Math inversion 
secret = int(res, 16) // ord('a')
log.success(f'secret integer = {secret}')

# FIXED: Calculate exact byte length cleanly using bit_length math
# Using len(str(secret)) was creating wrong key allocations for OpenSSL
byte_length = math.ceil(secret.bit_length() / 8) or 1
secret_bytes = secret.to_bytes(byte_length, "big")
secret_string = secret_bytes.decode("utf-8", errors="ignore").strip()
log.success(f'Decoded OpenSSL Key String: "{secret_string}"')

p.close()

# 5. Crack secret.enc using the correct key string context
res = run([
    "openssl", "enc", "-aes-256-cbc", "-d", 
    "-in", "secret.enc", # Ensure secret.enc is inside your active directory path
    "-pass", f"pass:{secret_string}"
], stdout=PIPE, stderr=PIPE, text=True)

if res.stdout:
    print("\n--- FLAG FOUND ---")
    print(res.stdout)
    print("------------------")
else:
    print("\n--- OpenSSL Error Log ---")
    print(res.stderr)
print('exit')

