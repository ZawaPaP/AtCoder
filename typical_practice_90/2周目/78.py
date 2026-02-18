N, M = map(int, input().split())

dic = {}

for _ in range(M):
    a, b = map(int, input().split())

    if a > b:
        dic[a] = dic.get(a, 0) + 1
    else:
        dic[b] = dic.get(b, 0) + 1

cnt = 0
for value in dic.values():
    if value == 1:
        cnt += 1
print(cnt)
