import time
start = time.time()
N = int(input())

P = [1]
for num in range(2, N + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
       P.append(num)

r = 0
for i in P:
    if N % i == 0:
        r += P.count(N // i)

print(r)
print(time.time() - start)
