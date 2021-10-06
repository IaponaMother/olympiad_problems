import time
start = time.time()
n, k = map(int, input().split(' '))

for i in range(k):
    a = str(input())

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)

if factorial(n) // (2 * factorial(n - 2)) > k:
    print('yes')
else:
    print('no')
print(time.time() - start)