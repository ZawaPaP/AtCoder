import math

N, K = map(int, input().split())

# 0.5の冪乗を保存する
# 17の理由は、10**5 < 2**17 のため
pows = []
for i in range(18):
    pows.append(pow(0.5, i))

ans = 0
for i in range(1, N + 1):
    if i >= K:
        ans += 1 / N
        continue
    temp = K / i
    ceiled_index = math.ceil(math.log2(temp))
    ans += pows[ceiled_index] / N

print(ans)
