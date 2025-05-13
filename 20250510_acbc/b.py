N, M = map(int, input().split())

A = list(map(int, input().split()))

ans = 0

while True:
    st = set(A)
    if len(st) < M:
        break
    A.pop()
    ans += 1

print(ans)
