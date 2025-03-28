N = int(input())
K = list(map(int, input().split()))

if N == 2:
    print(max(K))
    exit()

total_sum = sum(K)
half = total_sum // 2

possible_sums = {0}

for num in K:
    new_sums = set()
    for s in possible_sums:
        new_sums.add(s + num)
    possible_sums.update(new_sums)

min_max_value = total_sum
for s in possible_sums:
    if s <= half:
        min_max_value = min(min_max_value, max(total_sum - s, s))

print(min_max_value)

########
# 本来は 2^N 通りのグループ分けを試す方法で解けるが、ビット全探索が理解できなかった。
# 以下は、ビット全探索を使った解法
""" N = int(input())
K = list(map(int, input().split()))

min_max_value = float('inf')

# 2^N 通りのグループ分けを試す
for mask in range(1 << N):
    group_A = 0
    group_B = 0
    for i in range(N):
        if mask & (1 << i):
            group_A += K[i]
        else:
            group_B += K[i]
    max_value = max(group_A, group_B)
    min_max_value = min(min_max_value, max_value)

print(min_max_value) """

min_max_value = float('inf')

for mask in range(1 << N):
    group_A = 0
    group_B = 0
    for i in range(N):
        if mask & (1 << i):
            group_A += K[i]
        else:
            group_B += K[i]
    max_value =  max(group_A, group_B)
    min_max_value = min( max_value, min_max_value)
    

