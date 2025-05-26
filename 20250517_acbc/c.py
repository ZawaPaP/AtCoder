N = int(input())

P = list(map(int, input().split()))

mv = []

for i in range(1, N):
    if P[i - 1] < P[i]:
        mv.append("<")
    else:
        mv.append(">")

# 数えるのは、 <<<< >>>>> <<<<
# という山が来て谷が1つづつくるパターン
# その両側の <<< と <<< の数を数え上げて掛け算すると求めることができる

left_c = 0
right_c = 0
ans = 0
prev_mk = None

for v in mv:
    if v == ">":
        if prev_mk == "<":
            ans += left_c * right_c
            left_c = right_c
            right_c = 0
        prev_mk = ">"

    if v == "<":
        right_c += 1
        prev_mk = "<"

ans += left_c * right_c

print(ans)
