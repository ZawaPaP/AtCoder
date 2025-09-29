N = int(input())

A = list(map(int, input().split()))

# 山に降る雨の量をx1, x2, ... xNとする
# そうすると、x1 + x2 = 2A1, x2 + x3 = 2A2, ... xN-1 + xN = 2AN-1
# これを解くと 2X1 = 2A1 - 2A2 + 2A3 - 2A4 + ... + 2AN (Nは奇数)

x = 0
for i in range(N):
    if i % 2 == 0:
        x += A[i]
    else:
        x -= A[i]

# x1が決まれば、x2, x3, ... xNが決まる

ans = []
ans.append(x)
for i in range(N - 1):
    ans.append(2 * A[i] - ans[i])

print(*ans)
