N = int(input())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# 入り口は A[i]との合計距離が最小となる点
# つまり中央値となる
A.sort()
B.sort()

# 中央値を整数として取得
entry = A[N // 2]
goal = B[N // 2]

dist = 0
for i in range(N):
    # |S - Ai| + |Ai - Bi| + |Bi - G|
    dist += abs(entry - A[i])
    dist += B[i] - A[i]
    dist += abs(goal - B[i])

print(dist)
