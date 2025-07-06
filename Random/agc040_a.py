S = input()

tops = []


def calc_left_height(i, S):
    height = 0
    j = i
    while j >= 0 and S[j] == "<":
        height += 1
        j -= 1
    return height


def calc_right_height(i, S):
    height = 0
    j = i
    while j < len(S) and S[j] == ">":
        height += 1
        j += 1
    return height


if S[0] == ">":
    tops.append((0, calc_right_height(0, S)))

for i in range(1, len(S)):
    if S[i - 1] == "<" and S[i] == ">":
        tops.append((calc_left_height(i - 1, S), calc_right_height(i, S)))

if S[-1] == "<":
    tops.append((calc_left_height(len(S) - 1, S), 0))


def calc_partial_sums(n):
    return n * (n + 1) / 2


ans = 0
for top in tops:
    higher = top[0] if top[0] >= top[1] else top[1]
    lower = top[0] if higher != top[0] else top[1]
    ans += calc_partial_sums(higher)
    ans += calc_partial_sums(lower - 1)

print(int(ans))
