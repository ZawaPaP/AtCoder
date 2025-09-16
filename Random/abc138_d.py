
N, Q = map(int, input().split())

G = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

val = [0] * N
for _ in range(Q):
    p, x = map(int, input().split())
    p -= 1
    val[p] += x


def dfs_iterative():
    stack = [(0, -1)]  # (current_node, parent)

    while stack:
        v, parent = stack.pop()

        for child in G[v]:
            if child == parent:
                continue
            val[child] += val[v]
            stack.append((child, v))


dfs_iterative()
print(*val)
