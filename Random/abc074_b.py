N = int(input())
K = int(input())

X = list(map(int, input().split()))


ans = 0
for ball in X:
    dist_from_a = ball
    dist_from_b = K - ball

    if dist_from_a < dist_from_b:
        ans += dist_from_a * 2
    else:
        ans += dist_from_b * 2

print(ans)
