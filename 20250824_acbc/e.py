class UnionFind:
    def __init__(self, n: int):
        self.par = [-1] * n
        self.black_count = [0] * n  # 各連結成分の黒ノード数

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
        # 黒ノード数をマージ
        self.black_count[root_x] += self.black_count[root_y]
        self.black_count[root_y] = 0
        self.par[root_y] = root_x

    def toggle_color(self, x: int):
        root_x = self.root(x)
        self.black_count[root_x] += 1 if is_white[x] else -1

    def has_black(self, x: int) -> bool:
        root_x = self.root(x)
        return self.black_count[root_x] > 0


N, Q = map(int, input().split())

uf = UnionFind(N + 1)
ans = []

is_white = [True] * (N + 1)

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        uf.unite(q[1], q[2])
    elif q[0] == 2:
        uf.toggle_color(q[1])
        is_white[q[1]] = not is_white[q[1]]
    elif q[0] == 3:
        if uf.has_black(q[1]):
            ans.append("Yes")
        else:
            ans.append("No")

for i in ans:
    print(i)
