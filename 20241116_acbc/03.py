N, M = map(int, input().split())

X = list(map(int, input().split()))
A = list(map(int, input().split()))
XA = []
for i in range(M):
    XA.append([X[i], A[i]])

# Xの昇順にソート
# Xがすでに昇順されていると思いACできなかった
XA.sort()

# 2≤N≤2×10^9
# 1≤M≤2×10^5
# N のループではなく、Mのループで O(M)で求める

# 1番目のマスに石がない場合、不可能
if XA[0][0] != 1:
    print(-1)
    exit()


# 等差数列の和の公式
def count_moves(n, r):
    return r * (2 * n - r + 1) // 2


count = 0
for i in range(M - 1):
    if XA[i + 1][0] - XA[i][0] > XA[i][1]:
        print(-1)
        exit()
    elif XA[i + 1][0] - XA[i][0] < XA[i][1]:
        XA[i + 1][1] += XA[i][1] - (XA[i + 1][0] - XA[i][0])
        count += count_moves(XA[i][1] - 1, XA[i + 1][0] - XA[i][0])
    # X[i + 1] - X[i] == A[i]
    else:
        count += count_moves(XA[i][1] - 1, XA[i + 1][0] - XA[i][0])

if XA[-1][1] - 1 == N - XA[-1][0]:
    count += count_moves(XA[-1][1] - 1, N - XA[-1][0])
else:
    print(-1)
    exit()

print(count)
