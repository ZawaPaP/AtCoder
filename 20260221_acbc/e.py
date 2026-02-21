M, A, B = map(int, input().split())

# 数列にてM以上の最小値 m, nの両方がMで割り切れる場合、Mの倍数をいつか含む

lst = []
for i in range(1, M):
    for j in range(1, M):
        lst.append([i, j])

total = (M - 1) ** 2
ans = 0
for ls in lst:
    dig = A * ls[-1] + B * ls[-2]
    if M % dig == 0 or dig % M == 0:
        ans += 1
    else:
        continue

print(total - ans)
