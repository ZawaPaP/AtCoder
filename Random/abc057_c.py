N = int(input())

sqr = int(N ** 0.5)

ans = 1000000000000000
for i in range(1, sqr + 1):
    if N % i == 0:
        ans = min(ans, len(str(N // i)))
print(ans)
