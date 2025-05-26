N = int(input())

ans = 1
temp = 1
for _ in range(0, N // 2):
    if temp * 2 <= N:
        temp *= 2
        ans = temp

print(ans)
