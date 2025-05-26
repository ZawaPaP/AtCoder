A, B = map(int, input().split())

outlet = 1
ans = 0
while outlet < B:
    ans += 1
    outlet += A - 1

print(ans)
