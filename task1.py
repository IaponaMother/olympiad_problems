import time
start = time.time()
planets, p = map(int, input().split(' '))
param = list(map(int, input().split(' ')))
s = sum(param)
names = []
scores = []
for i in range(planets):
    pl = list(map(str, input().split(' ')))
    n = pl[0]
    c = [int(j) for j in pl[1:]]
    x = 0
    for k in range(len(c)):
        if c[k] >= param[k]:
            x += 1
    if x >= len(param):
        names.append(n)
        scores.append(sum(c))

t = sum(scores)//len(scores)
for i in range(len(scores)):
    if scores[i] >= t:
        print(names[i])
print(time.time() - start)


"""4 3
1 2 2
MERCURY 1 2 1
VENUS 2 2 2
MARS 3 3 4
TAUKITAE 3 3 3"""
