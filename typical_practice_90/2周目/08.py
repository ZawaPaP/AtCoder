N = int(input())
S = input()

T = "atcoder"
MOD = 10**9 + 7

# DP? iまでの文字列での各部分文字列の作り方総数
# DP[i] について、Tの先頭i文字を部分列として作る通り数

dp = [0 for _ in range(8)]
dp[0] = 1

for ch in S:
    for j in range(len(T) - 1, -1, -1):
        if ch == T[j]:
            dp[j + 1] += dp[j]

print(dp[-1] % MOD)
