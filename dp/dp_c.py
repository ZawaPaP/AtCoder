N = int(input())

Happiness = [[0, 0, 0] for _ in range(N)]

a, b, c = map(int, input().split())
Happiness[0][0] = a
Happiness[0][1] = b
Happiness[0][2] = c

for i in range(1, N):
    a, b, c = map(int, input().split())
    Happiness[i][0] = max(Happiness[i - 1][1] + a, Happiness[i - 1][2] + a)
    Happiness[i][1] = max(Happiness[i - 1][0] + b, Happiness[i - 1][2] + b)
    Happiness[i][2] = max(Happiness[i - 1][0] + c, Happiness[i - 1][1] + c)

print(max(max(Happiness[N - 1][0], Happiness[N - 1][1]), Happiness[N - 1][2]))
