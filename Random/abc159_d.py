import math

N = int(input())

A = list(map(int, input().split()))

dic = {}

for a in A:
    dic[a] = dic.get(a, 0) + 1

# デフォルトの状態で、数が同じくなるようにボールを選び出す方法
combinations = {}

# その数が１減ったとして、ボールを選び出す方法
limited_combinations = {}

for num, value in dic.items():
    if value < 2:
        combinations[num] = 0
    else:
        combinations[num] = math.comb(value, 2)
    if value > 2:
        limited_combinations[num] = math.comb(value - 1, 2)
    else:
        limited_combinations[num] = 0

sum_combinations = sum(combinations.values())
# k = 1 ~ N についてk番目のボールを除いて、combinationを計算
for a in A:
    ans = sum_combinations - combinations[a] + limited_combinations[a]
    print(ans)
