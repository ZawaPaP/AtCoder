N = int(input())
A = list(map(int, input().split()))

balls = [0] * (N + 1)

for i in range(N, 0, -1):
    # 自分の倍数のballsの数を確認
    balls_c = 0
    for j in range(i * 2, N + 1, i):
        balls_c += balls[j]
    if balls_c % 2 != A[i - 1]:
        balls[i] = 1

if sum(balls) == 0:
    print(0)
else:
    print(balls.count(1))
    for i in range(1, N + 1):
        if balls[i] == 1:
            print(i, end=" ")
    print()
