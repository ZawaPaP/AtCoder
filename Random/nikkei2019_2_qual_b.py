N = int(input())

D = list(map(int, input().split()))

MOD = 998244353

if D[0] != 0:
    print(0)
    exit()

D.sort()

count = [0] * (max(D) + 1)

for i in range(1, N):
    if D[i] - D[i - 1] > 1:
        print(0)
        exit()
    count[D[i]] += 1

if len(count) == 1:
    print(1)
    exit()
if count[0] != 0:
    print(0)
    exit()

ans = 1
for i in range(2, len(count)):
    ans *= count[i - 1] ** count[i]

print(ans % MOD)
