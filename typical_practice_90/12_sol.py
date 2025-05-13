class UnionFind:
    def __init__(self, size):
        self.par = [-1] * size

    def root(self, pos):
        if self.par[pos] == -1:
            return pos
        self.par[pos] = self.root(self.par[pos])
        return self.par[pos]

    def union(self, u, v):
        ru = self.root(u)
        rv = self.root(v)
        if ru == rv:
            return
        self.par[ru] = rv

    def same(self, u, v):
        return self.root(u) == self.root(v)


H, W = map(int, input().split())
Q = int(input())

uf = UnionFind(H * W)
grid = [[False] * W for _ in range(H)]  # False = 白, True = 赤


def index(r, c):
    return r * W + c


queries = []
for _ in range(Q):
    query = list(map(int, input().split()))
    queries.append(query)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for query in queries:
    if query[0] == 1:
        r, c = query[1] - 1, query[2] - 1
        grid[r][c] = True
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc]:
                uf.union(index(r, c), index(nr, nc))
    else:
        r1, c1, r2, c2 = query[1] - 1, query[2] - 1, query[3] - 1, query[4] - 1
        if grid[r1][c1] and grid[r2][c2] and uf.same(index(r1, c1), index(r2, c2)):
            print("Yes")
        else:
            print("No")
