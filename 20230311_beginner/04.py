
#unsolved

import queue
N, M = map(int, input().split())

G = [list() for i in range(N + 1)]

for i in range(1, M + 1):
    tmp = input().split()
    a = int(tmp[0])
    b = tmp[1]
    c = int(tmp[2])
    d = tmp[3]
    if b == "R":
        G[a].append(c)
    elif d == "R":
        G[c].append(a)

def dfs(pos, G, visited):
    global x
    if visited[pos] == True:
        return
    elif G[pos]:
        visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i, G, visited)
        else:
            x += 1

visited = [False] * (N + 1)
x = y = 0


for i in range(1, N + 1):
    dfs(i, G, visited)


for i in range(1, N + 1):
    if visited[i] == False:
        y += 1

print(x, y)