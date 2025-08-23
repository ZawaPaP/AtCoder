N, M = map(int, input().split())

S = []

for _ in range(M):
    temp = list(map(int, input().split()))
    S.append(temp[1:])

P = list(map(int, input().split()))

# スイッチは最大10個なので、すべてのスイッチの状態の組み合わせはmax 2 ** 10 = 1024通りしかない
# これらの組み合わせを全て試す

ans = 0
for i in range(2 ** N):
    for j in range(M):
        count = 0
        for k in S[j]:
            if i & (1 << (k - 1)):
                count += 1
        if count % 2 != P[j]:
            break
    else:
        ans += 1

print(ans)
