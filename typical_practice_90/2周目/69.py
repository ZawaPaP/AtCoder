N, K = map(int, input().split())

MOD = 10**9 + 7
# Kは3種類以上が必要 かつ K * K - 1 * (K - 2)^(N - 2)になるのでは？

ans = 0
tmp = 1

# K < 3の時のケース
if K < 3 and N > K:
    print(0)
    exit()

# K < 3 かつ N <= K or  K >= 3の時のケース
if N < 3:
    for n in range(N):
        tmp *= K
        K -= 1
    print(tmp % MOD)
    exit()
else:
    tmp = K * (K - 1)
    tmp *= pow(K - 2, N - 2, MOD)
    print(tmp % MOD)
