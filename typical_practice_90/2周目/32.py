import itertools

N = int(input())

A = []
for _ in range(N):
    a = list(map(int, input().split()))
    A.append(a)

M = int(input())
Rumors = {}
for _ in range(M):
    x, y = map(int, input().split())
    if x in Rumors:
        Rumors[x].append(y)
    else:
        Rumors[x] = [y]

    if y in Rumors:
        Rumors[y].append(x)
    else:
        Rumors[y] = [x]

perm = itertools.permutations(list(i for i in range(1, N + 1)), N)

ans = float('inf')
for p in perm:
    lst = list(p)

    sum = 0
    finish = True
    for section, runner in enumerate(p):
        if section > 0 and runner in Rumors and p[section - 1] in Rumors[runner]:
            finish = False
            break
        sum += A[runner - 1][section]
    if finish:
        ans = min(ans, sum)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
