N = int(input())

S = set()
counts = {}

for _ in range(N):
    s = input()
    s = "".join(sorted(s))

    if s in S:
        counts[s] = counts.get(s, 0) + 1
    else:
        S.add(s)

ans = 0
for v in counts.values():
    ans += (v + 1) * v // 2

print(ans)
