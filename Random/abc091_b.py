N = int(input())
S = {}

for _ in range(N):
    s = input()
    if s in S:
        S[s] += 1
    else:
        S[s] = 1

M = int(input())
T = {}

for _ in range(M):
    t = input()
    if t in T:
        T[t] += 1
    else:
        T[t] = 1


ans = 0
for s in S:
    temp = S[s]
    if s in T:
        temp -= T[s]
    ans = max(ans, temp)

print(ans)
