N = int(input())

A = [list(map(int, input().split())) for _ in range(2)]


ans = [[0] * N for _ in range(2)]
ans[0][0] = A[0][0]
ans[1][0] = A[1][0] + ans[0][0]

for i in range(1, N):
    ans[0][i] = ans[0][i - 1] + A[0][i]
    ans[1][i] = max(ans[1][i - 1], ans[0][i]) + A[1][i]

print(ans[1][N - 1])
