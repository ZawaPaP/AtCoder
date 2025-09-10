N = int(input())

robots = []
for _ in range(N):
    x, l = map(int, input().split())
    robots.append((x, l))

robots.sort(key=lambda x: x[0])

ans = [True] * N
for i in range(len(robots) - 1):
    if ans[i] == False:
        continue
    p, arm = robots[i]
    # 左が右を内包しているケース
    if p + arm > robots[i + 1][0] + robots[i + 1][1]:
        ans[i] = False
    # 重なっているケース or 内包されているケース
    elif p + arm > robots[i + 1][0] - robots[i + 1][1]:
        ans[i + 1] = False
    else:
        continue

print(ans.count(True))
