N, M = map(int, input().split())

passed = set()
penalties = {}

for _ in range(M):
    p, S = map(str, input().split())
    p = int(p)

    if p not in passed:
        if S == "AC":
            passed.add(p)
        else:
            penalties[p] = penalties.get(p, 0) + 1

total_penalty = sum(penalties.get(p, 0) for p in passed)

print(len(passed), total_penalty)
