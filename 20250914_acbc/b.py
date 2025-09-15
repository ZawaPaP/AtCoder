N = int(input())
L = list(map(int, input().split()))

# 部屋０からいける部屋

max_reachable_from_zero = 0
for i in range(N):
    if L[i] != 0:
        max_reachable_from_zero = i
        break

max_reachable_from_end = 0
for i in range(N - 1, -1, -1):
    if L[i] != 0:
        max_reachable_from_end = i
        break

print(max_reachable_from_end - max_reachable_from_zero)
