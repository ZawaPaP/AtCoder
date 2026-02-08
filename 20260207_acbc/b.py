N, K = map(int, input().split())


count = 0
for i in range(1, N + 1):
    str_i = str(i)
    lst = list(map(int, str_i))
    if sum(lst) == K:
        count += 1

print(count)
