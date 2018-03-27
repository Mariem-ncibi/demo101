import hashlib

msg=hashlib.md5(b"Hello World").digest()
print(msg)
