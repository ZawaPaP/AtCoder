N = int(input())
A = list(map(int, input().split()))


candidates = {}


for a in A:
    for i in range(-1, 2):
        temp = a + i
        candidates[temp] = candidates.get(temp, 0) + 1

ans = 0

for v in candidates.values():
    ans = max(ans, v)
print(ans)
