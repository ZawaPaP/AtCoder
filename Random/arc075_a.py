N = int(input())

S = []

# 10の倍数ではない最小値
smallest_non_ten = float("INF")

for _ in range(N):
    s = int(input())
    if s % 10 != 0:
        smallest_non_ten = min(smallest_non_ten, s)
    S.append(s)

total = sum(S)

if total % 10 != 0:
    print(total)
    exit()
else:
    if smallest_non_ten != float("INF"):
        print(total - smallest_non_ten)
        exit()
    else:
        print(0)
