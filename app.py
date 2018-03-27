import hashlib

msg=hashlib.sha512(b"Hi World").digest()
print(msg)
