import math

N, K = map(int, input().split())

A = list(map(int, input().split()))

# 最終的に全て１に収束する
# Aのうち、1を含む長さKの区間を選んで、Kづつ1にしていく
# まず左側を実施。あまりが出ないように最初に1を含む区間を選ぶ
# その後、右側を実施。

count = 0


count += 1
count += math.ceil((len(A) - K) / (K - 1))

print(count)
