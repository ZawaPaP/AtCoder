#
# M進数をN進数に変換
#


def convert_base(m, a, n):
    decimal_val = int(str(a), m)

    if decimal_val == 0:
        return "0"

    res = ""
    while decimal_val > 0:
        res = str(decimal_val % n) + res
        decimal_val //= n

    return res


N, K = map(int, input().split())

for _ in range(K):
    # N は８進数なので9進数に変換する
    lst_base9 = list(map(str, convert_base(8, N, 9)))
    for i in range(len(lst_base9)):
        if lst_base9[i] == "8":
            lst_base9[i] = "5"
    N = int("".join(lst_base9))

print(N)
