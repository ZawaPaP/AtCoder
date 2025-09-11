N = int(input())

robots = []
for _ in range(N):
    x, l = map(int, input().split())
    s = x - l
    e = x + l
    robots.append((s, e))

robots.sort(key=lambda x: x[1])

ans = [True] * N
prev = float("-inf")
for i in range(len(robots)):
    if prev <= robots[i][0]:
        prev = robots[i][1]
    else:
        ans[i] = False

print(ans.count(True))
