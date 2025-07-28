N, M = map(int, input().split())

ans = 0

if N == 1 and M == 1:
    print(0)
    exit()

if N > M // 2:
    ans += M // 2
else:
    ans += N
    M -= N * 2

    if M > 3:
        ans += M // 4

print(ans)
