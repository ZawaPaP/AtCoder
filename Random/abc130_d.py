N, K = map(int, input().split())

A = list(map(int, input().split()))

prev_l = 0
l = 0
r = 0
sum = 0
ans = 0
for i in range(N):
    sum += A[i]
    if sum >= K:
        r = i
        while sum >= K and l <= r:
            sum -= A[l]
            l += 1
        l -= 1
        ans += (l - prev_l + 1) * (N - r)
        l += 1
        prev_l = l

print(ans)
