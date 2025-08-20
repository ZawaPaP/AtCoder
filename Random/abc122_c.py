N, Q = map(int, input().split())

S = input()

# i 文字目までに AC が出現した回数
AC_count = [0] * N

for i in range(N - 1):
    if S[i] == "A" and S[i + 1] == "C":
        AC_count[i + 1] = AC_count[i] + 1
    else:
        AC_count[i + 1] = AC_count[i]

for _ in range(Q):
    l, r = map(int, input().split())
    print(AC_count[r - 1] - AC_count[l - 1])
