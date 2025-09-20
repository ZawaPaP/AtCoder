s = input()
t = input()

# DPテーブルの初期化（1-indexedで考える）
dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

# DPの計算
for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

# 最長共通部分列の長さ
# print(dp[len(s)][len(t)])


def reconstruct_lcs(dp, s, t):
    i, j = len(s), len(t)
    lcs = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            lcs.append(s[i - 1])
            i -= 1
            j -= 1
    return "".join(lcs)


print(reconstruct_lcs(dp, s, t)[::-1])
