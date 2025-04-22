N, M = map(int, input().split())
slope_groups = {}

for _ in range(M):
    a, b = map(int, input().split())
    # (a+b) mod N で傾きを分類
    slope = (a + b) % N
    if slope in slope_groups:
        slope_groups[slope] += 1
    else:
        slope_groups[slope] = 1

# 交わらない直線ペアの数
non_crossing_pairs = 0
for count in slope_groups.values():
    if count > 1:
        # 同じ傾きを持つ直線同士は交わらない
        non_crossing_pairs += (count * (count - 1)) // 2

# 全体の組み合わせから交わらないペアを引く
total_pairs = (M * (M - 1)) // 2
crossing_pairs = total_pairs - non_crossing_pairs

print(crossing_pairs)
