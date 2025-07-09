N = int(input())
S = input()

left = [0] * 26
right = [0] * 26

for s in S:
    char = ord(s)
    right[char - 97] += 1

ans = 0
count = 0
for s in S:
    unicode_int = ord(s) - 97

    right[unicode_int] -= 1
    left[unicode_int] += 1

    if left[unicode_int] == 1 and right[unicode_int]:
        count += 1
    if left[unicode_int] > 1 and right[unicode_int] == 0:
        count -= 1
    ans = max(ans, count)

print(ans)
