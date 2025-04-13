N, K = map(int, input().split())
S = input()

dict_map = {}


def map_string(str):
    for i in range(len(str)):
        if not dict_map.get(i):
            dict_map[i] = str[i]
        else:
            if dict_map[i] == str[i]:
                continue
            elif dict_map[i] != '?':
                dict_map[i] = '?'


# dp[i][k][prev] : i文字目まで見て、残りk個の'o'があり、前の文字がprevである場合の文字列
# prev: 0='.', 1='o'
dp = [[[None for _ in range(2)] for _ in range(K+1)] for _ in range(N+1)]

# 初期状態
if S[0] == 'o':
    if K > 0:
        dp[0][K-1][1] = S[0]
elif S[0] == '.':
    dp[0][K][0] = S[0]
else:  # S[0] == '?'
    if K > 0:
        dp[0][K-1][1] = 'o'
    dp[0][K][0] = '.'

for i in range(1, N):
    for k in range(K+1):
        # 前の文字が'.'の場合
        if dp[i-1][k][0] is not None:
            if S[i] == 'o' and k > 0:
                dp[i][k-1][1] = dp[i-1][k][0] + 'o'
            elif S[i] == '.':
                dp[i][k][0] = dp[i-1][k][0] + '.'
            elif S[i] == '?':
                if k > 0:
                    dp[i][k-1][1] = dp[i-1][k][0] + 'o'
                dp[i][k][0] = dp[i-1][k][0] + '.'

        # 前の文字が'o'の場合
        if dp[i-1][k][1] is not None:
            if S[i] == '.':
                dp[i][k][0] = dp[i-1][k][1] + '.'
            elif S[i] == '?':
                dp[i][k][0] = dp[i-1][k][1] + '.'

# 解の構築
result = None
for k in range(K+1):
    if k == 0:  # ちょうどK個の'o'を使った場合のみ
        if dp[N-1][k][0] is not None:
            result = dp[N-1][k][0]
            map_string(result)
        if dp[N-1][k][1] is not None:
            result = dp[N-1][k][1]
            map_string(result)

print("".join(dict_map.values()))
