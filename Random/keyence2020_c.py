N, K, S = map(int, input().split())

ans = []

for i in range(N):
    if i < K:
        ans.append(S)
    else:
        ans.append(S + 1) if S != 10**9 else ans.append(S - 1)

print(" ".join(map(str, ans)))
