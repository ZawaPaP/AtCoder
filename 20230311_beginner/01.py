S = input()

ans = ""
ans += S[1]
ans += S[0]

for i in range(1, len(S) // 2):
    ans += S[(2 * i) + 1]
    ans += S[(2*i)]    
print(ans)
