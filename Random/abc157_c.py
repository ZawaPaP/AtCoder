N, M = map(int, input().split())

rules = {}

for _ in range(M):
    s, c = map(int, input().split())

    if s == 1 and c == 0 and N != 1:
        print(-1)
        exit()

    if s in rules and rules[s] != c:
        print(-1)
        exit()
    else:
        rules[s] = c

ans = 0

for i in range(1, N + 1):
    if i == 1:
        # 最上位桁の場合、制約がない場合は最小値（N=1なら0、それ以外なら1）
        temp = rules.get(i, 0 if N == 1 else 1)
    else:
        temp = rules.get(i, 0)
    ans = ans * 10 + temp

print(ans)
