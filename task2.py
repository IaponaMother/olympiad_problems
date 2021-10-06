import time
start = time.time()

n, k = map(int, input().split(' '))
ships = list(map(int, input().split(' ')))
_ships = ships.copy()
it = [i + 1 for i in range(-1, n - 1)]
res1 = [0] * n
res2 = res1.copy()
t = 0

while len(it) > 0:
    for i in it:
        if (i - t) % k == 0:
            res1[i] = max(ships)
            res2[i] = min(_ships)
            ships.pop(ships.index(max(ships)))
            _ships.pop(_ships.index(min(_ships)))
            it.pop(it.index(i))
    t += 1

print(" ".join(map(str, res1)))
print(" ".join(map(str, res2)))
print(time.time() - start)
"""6 2
3 2 7 10 4 5

7 3 10 2 5 4
3 7 2 10 4 5"""



"""7 3
1 2 3 4 5 6 7

5 4 3 6 2 1 7
1 5 6 2 7 4 3"""


"""2 100
1 2
2 1
1 2"""
