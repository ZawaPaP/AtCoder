N = int(input())

D = list(map(int, input().split()))

D.sort()

ans = D[N // 2] - D[N // 2 - 1]

print(ans)
