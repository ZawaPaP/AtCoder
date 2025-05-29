S = input()

target_num = 753

left = 0
right = 2

ans = float("inf")

while right < len(S):
    num = S[left : right + 1]
    ans = min(ans, abs(target_num - int(num)))
    left += 1
    right += 1

print(ans)
