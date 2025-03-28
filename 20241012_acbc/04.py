""" S = input()

dict = {}

for i in range(len(S)):
    if S[i] in dict:
        dict[S[i]].append(i)
    else:
        dict[S[i]] = [i]

cnt = 0
for key in dict:
    if len(dict[key]) < 2:
        continue
    lst = []
    tmp = sum(dict[key]) - dict[key][0] - dict[key][-1]
    cnt += (dict[key][-1] - dict[key][0] - 1) - (len(dict[key]) - 1)

print(cnt)
 """

# 問題文から アルファベット単位で考えることができたのはよかった
# しかし、その後に2重ループを回してしまったのが誤り

# 累積和を使って解くのも気がつかなかった
# 回文の個数の数え方を考えた時に、ans += (i - 1) * cnt[v] - prefix_sum[v]
# という式が出てくることを考えつけるかどうかが大事だった。
# これは、i番目のアルファベットを基準として、回文の個数を考えている
# 回文の個数は単純に i より前の同じアルファベットとのインデックスの差 - 1 で求められる。
# そのため、i より前の同じアルファベットの個数が cnt[v] 個あるとすると、
# もし、cnt[v] のインデックスが 0 であれば、回文の個数は cnt[v] * (i - 1) 個である。
# しかし、実際にはインデックスはそれぞれ異なるため、その分を引く必要がある。
# そのため、prefix_sum[v] には、cnt[v] のインデックスの合計が格納されている。


# https://atcoder.jp/contests/abc375/tasks/abc375_d

S = input()

cnt = [0] * 26
prefix_sum = [0] * 26
ans = 0

n = len(S)

for i in range(n):
    v = ord(S[i]) - ord("A")
    ans += (i - 1) * cnt[v] - prefix_sum[v]
    cnt[v] += 1
    prefix_sum[v] += i

print(ans)
