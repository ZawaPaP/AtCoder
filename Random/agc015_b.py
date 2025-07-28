S = list(input())


len_s = len(S)

ans = 0
for i in range(len_s):
    if S[i] == "U":
        ans += i * 2
        ans += len_s - i - 1
    else:
        ans += i
        ans += (len_s - i - 1) * 2

print(ans)
