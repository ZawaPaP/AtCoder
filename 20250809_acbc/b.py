S = input()


def calc_fill_rate(s):
    """文字列sの充填率を計算する"""
    if len(s) < 3:
        return 0

    # 先頭と末尾が両方とも"t"でない場合は0
    if s[0] != "t" or s[-1] != "t":
        return 0

    # "t"の個数を数える
    t_count = s.count("t")

    # 充填率 = (tの個数 - 2) / (長さ - 2)
    return (t_count - 2) / (len(s) - 2)


# すべての部分文字列を試す
ans = 0
n = len(S)

for i in range(n):
    for j in range(i + 3, n + 1):  # 長さ3以上
        substring = S[i:j]
        fill_rate = calc_fill_rate(substring)
        ans = max(ans, fill_rate)

print(ans)
