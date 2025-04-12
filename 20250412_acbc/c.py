N, K = map(int, input().split())

MOD = 1000000000

k_left = 0
k_right = 0
k_sum = 0
A = [1] * (N + 1)

for i in range(N + 1):
    if i < K:
        continue
    if i == K:
        k_left = i - K
        k_right = i - 1
        k_sum = i
        A[i] = k_sum % MOD
    else:
        k_sum -= A[k_left]
        k_left += 1
        k_right += 1
        k_sum += A[k_right]
        A[i] = k_sum % MOD

print(A[N])
