N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 端から常に最大限倒すことで、最大数のモンスターを倒せる

ans = 0

remaining_power = 0
for i in range(N):
    if A[i] <= B[i] + remaining_power:
        ans += A[i]
        remaining_power = B[i] - max(0, A[i] - remaining_power)

    else:
        ans += B[i] + remaining_power
        remaining_power = 0

ans += min(A[N], remaining_power)

print(ans)
