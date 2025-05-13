class UnionFind:
    def __init__(self, n: int):
        self.par = [-1] * n

    def root(self, x: int) -> int:
        if self.par[x] == -1:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def same(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def unite(self, x: int, y: int):
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        self.par[root_y] = root_x


N, Q = map(int, input().split())

uf = UnionFind(N + 1)
ans = []

for _ in range(Q):
    P, A, B = map(int, input().split())

    if P == 0:
        uf.unite(A, B)

    elif P == 1:
        temp = uf.same(A, B)
        if temp:
            ans.append("Yes")
        else:
            ans.append("No")

for i in ans:
    print(i)
