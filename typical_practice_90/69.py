N, K = map(int, input().split())

MOD = 10**9 + 7

if N == 1:
    print(K % MOD)
    exit()

if N == 2 and K > 1:
    print(K % MOD * (K - 1) % MOD)
    exit()

if K > 2:
    ans = pow((K - 2), (N - 2), MOD)
    ans *= K % MOD
    ans *= K - 1
    print(ans % MOD)
    exit()

print(0)
