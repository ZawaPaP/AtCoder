N, A, B = map(int, input().split())


count = 0
balls = A + B

div = N // balls
temp = N % balls

ans = div * A
ans += min(temp, A)

print(ans)
