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
        if len(ships) == 0: break
    t += 1


print(" ".join(map(str, res1)))
print(" ".join(map(str, res2)))