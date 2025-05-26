N = int(input())

D, X = map(int, input().split())


ate = 0

for _ in range(N):
    a = int(input())

    # 1日目
    ate += 1

    temp = 1 + a
    while temp <= D:
        ate += 1
        temp += a

print(ate + X)
