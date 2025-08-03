N = int(input())

p = list(map(int, input().split()))

ans = 0
temp = 0
for i in range(N):
    if p[i] == i + 1:
        temp += 1
    else:
        if temp > 0:
            ans += (temp + 1) // 2
            temp = 0
if temp > 0:
    ans += (temp + 1) // 2

print(ans)
