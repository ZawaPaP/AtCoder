N = int(input())
D = list(map(int, input().split()))

M = int(input())
T = list(map(int, input().split()))

if N < M:
    print("NO")
    exit()

D_map = {}
for d in D:
    D_map[d] = D_map.get(d, 0) + 1

for t in T:
    if t not in D_map:
        print("NO")
        exit()
    D_map[t] -= 1
    if D_map[t] < 0:
        print("NO")
        exit()

print("YES")
