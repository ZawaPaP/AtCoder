N, M = map(int, input().split())

ans = 0

if N > 2 and M > 2:
    ans = (N - 2) * (M - 2)
else:
    for i in range(N):
        for j in range(M):
            temp = 0
            if i - 1 >= 0:
                temp += 1
            if i + 1 < N:
                temp += 1
            if j - 1 >= 0:
                temp += 1
            if j + 1 < M:
                temp += 1
            if i - 1 >= 0 and j - 1 >= 0:
                temp += 1
            if i - 1 >= 0 and j + 1 < M:
                temp += 1
            if i + 1 < N and j - 1 >= 0:
                temp += 1
            if i + 1 < N and j + 1 < M:
                temp += 1
            if temp % 2 == 0:
                ans += 1

print(ans)
