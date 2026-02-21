S = input()

ans = 0
c = 0
while c < len(S):
    temp = 0
    while c < len(S) and (S[c] == "A" or S[c] == "C" or S[c] == "G" or S[c] == "T"):
        temp += 1
        c += 1
    ans = max(ans, temp)
    c += 1
print(ans)
