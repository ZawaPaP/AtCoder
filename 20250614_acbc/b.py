N, Q = map(int, input().split())

X = list(map(int, input().split()))

balls = [0] * (N + 1)
ans = []

for x in X:
    if x >= 1:
        balls[x] += 1
        ans.append(x)

    else:
        min_value = 10**9
        min_index = 0
        for i in range(1, N + 1):
            if balls[i] < min_value:
                min_value = balls[i]
                min_index = i

        balls[min_index] += 1
        ans.append(min_index)

print(*ans)
