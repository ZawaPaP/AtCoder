N = int(input())

A = list(map(int, input().split()))

# 各Aの要素について、それぞれ何回２で割れるかを求める

ans = 0
for i in range(N):
    count = 0
    while A[i] % 2 == 0:
        A[i] //= 2
        count += 1
    ans += count

print(ans)
