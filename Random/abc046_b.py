N, K = map(int, input().split())


if N == 1:
    print(K)
    exit()

# 1こ目の塗り方はK通り
# 2こ目以降は K - 1通り

ans = K

for _ in range(N - 1):
    ans *= K - 1

print(ans)
