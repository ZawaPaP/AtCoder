K = int(input())

MOD = 10**9 + 7

if K % 9 != 0:
    print(0)
    exit()

# dpを使って、桁の合計が 0 ~ K になるような数の個数を求める
dp = [0] * (K + 1)
dp[0] = 1

for i in range(1, K + 1):
    for j in range(1, 10):
        if i - j >= 0:
            dp[i] += dp[i - j]
            dp[i] %= MOD

print(dp[K])
