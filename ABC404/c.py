from collections import deque

N, M = map(int, input().split())

mp = {}

for _ in range(M):
    A, B = map(int, input().split())

    if A in mp:
        mp[A].append(B)
    else:
        mp[A] = [B]

    if B in mp:
        mp[B].append(A)
    else:
        mp[B] = [A]

# 辺が2本を超える頂点が存在する場合、サイクルグラフではない
for value in mp.values():
    if len(value) > 2:
        print("No")
        exit()

if 1 not in mp:
    print("No")
    exit()

# 1から始めて、全ての頂点を一度しか通らずに全ての頂点を通ることができるかどうか
visited = [False] * N

Q = deque()
Q.append(1)
visited[0] = True

while Q:
    current = Q.popleft()

    if current not in mp:
        print("No")
        exit()

    for i in mp[current]:
        if not visited[i - 1]:
            Q.append(i)
            visited[i - 1] = True
            break

for i in visited:
    if not i:
        print("No")
        exit()
print("Yes")
