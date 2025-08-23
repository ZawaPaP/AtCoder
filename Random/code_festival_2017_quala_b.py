N, M, K = map(int, input().split())

if K == 0 or K == N * M:
    print("Yes")
    exit()

for x in range(0, M + 1):
    for y in range(0, N + 1):
        if x * N + (M - 2*x) * y == K:
            print("Yes")
            exit()

print("No")
