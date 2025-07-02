N = int(input())

A = list(map(int, input().split()))

A.sort(reverse=True)

ans = 0

for i in range(0, 2 * N, 2):
    ans += A[i + 1]

print(ans)
