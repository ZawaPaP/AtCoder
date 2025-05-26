N, K = map(int, input().split())


temp = N % K
ans = min(temp, abs(temp - K))

print(ans)
