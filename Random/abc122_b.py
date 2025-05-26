S = input()

# ACGTの文字をセットとして定義
ATCG = {"A", "C", "G", "T"}

current_length = 0  # 現在の連続長
max_length = 0  # 最大の連続長

for char in S:
    if char in ATCG:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0

print(max_length)
