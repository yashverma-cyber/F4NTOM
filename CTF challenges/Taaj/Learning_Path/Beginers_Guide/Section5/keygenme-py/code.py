import hashlib
import base64

username_trial = b"BENNETT"
dynamic_key = ""
positions = [4,5,3,6,2,7,1,8]

for i in positions:
	dynamic_key += hashlib.sha256(username_trial).hexdigest()[i]

print(dynamic_key)