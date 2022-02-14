p = "00991234567890987123456123"
h = hash("123")
r = 0
for j in range(len(p) - 2):
    if hash(str(p[j:j + 3]).encode()) == h:
        r += 1
    j += 1
print(h)
print(r)


"""
from hashlib import sha224
p = "1234567890987123456123"
h = sha224("123".encode()).hexdigest()
r = 0
for j in range(len(p) - 2):
    if (sha224(p[j:j + 3].encode())).hexdigest() == h:
        r += 1
    j += 1
print(h)
print(r)
"""
