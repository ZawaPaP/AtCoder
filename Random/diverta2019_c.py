N = int(input())

S = [input() for _ in range(N)]

# 各文字列のABをカウント
# その後、末尾のAと先頭のBをカウント

last_a = 0
first_b = 0
both = 0
ab_count = 0

for s in S:
    if s.endswith("A") and s.startswith("B"):
        both += 1
    elif s.endswith("A"):
        last_a += 1
    elif s.startswith("B"):
        first_b += 1
    for i in range(1, len(s)):
        if s[i - 1] == "A" and s[i] == "B":
            ab_count += 1


# bothが2つ以上あれば、(both + 1) // 2 のABが作れる
both_comb = both - 1 if both > 0 else 0

# both(both_comb)の両サイドについて、last_a, first_bが1以上あればそれぞれ1つずつABが作れる
if both > 0 and last_a >= 1:
    both_comb += 1
    last_a -= 1
if both > 0 and first_b >= 1:
    both_comb += 1
    first_b -= 1

# 残ったlast_a, first_bを組み合わせてABを作る
comb = min(last_a, first_b)

print(ab_count + both_comb + comb)
