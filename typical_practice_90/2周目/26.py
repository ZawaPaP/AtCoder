from collections import deque

N = int(input())

G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())

    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

# edgeを2種類に分類していく

color = [-1] * N
color[0] = 0
q = deque([0])

while q:
    curr = q.popleft()

    for nxt in G[curr]:
        if color[nxt] != -1:
            continue
        color[nxt] = 1 - color[curr]
        q.append(nxt)

A = [i + 1 for i in range(N) if color[i] == 0]
B = [i + 1 for i in range(N) if color[i] == 1]

if len(A) >= N // 2:
    print(*A[:N // 2])
else:
    print(*B[:N // 2])
