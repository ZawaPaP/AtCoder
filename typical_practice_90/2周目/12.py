class UnionFind():
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

    def root(self, x):
        # 親がない
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    # x, y が同じ rootを持つか (同じグループか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # xを含むグループとyを含むグループを併合する
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return False

        # rankは木の高さの上界
        # 高さが低い方を、高い方の根にぶら下げる
        # 高さが同じなら、１段だけ追加となる
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx

        # ryをrxの子とする
        self.par[ry] = rx

        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

        self.siz[rx] += self.siz[ry]
        return True

    # x を含むグループのサイズを求める
    def size(self, x):
        return self.siz[self.root(x)]


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

H, W = map(int, input().split())
Q = int(input())

red = [[False] * W for _ in range(H)]

uf = UnionFind(W * H)


def idx(r, c):
    return r * W + c


ans = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        r, c = q[1] - 1, q[2] - 1
        red[r][c] = True
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < H and 0 <= nc < W and red[nr][nc]:
                uf.unite(idx(r, c), idx(nr, nc))

    else:
        r1, c1, r2, c2 = q[1] - 1, q[2] - 1, q[3] - 1, q[4] - 1
        ans.append(uf.issame(idx(r1, c1), idx(r2, c2))
                   and red[r1][c1] and red[r2][c2])

for a in ans:
    if a:
        print("Yes")
    else:
        print("No")
