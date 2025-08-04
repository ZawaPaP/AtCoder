N = int(input())

A = []
B = []

for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

ans = 0
for i in reversed(range(N)):
    amari = (A[i] + ans) % B[i]
    if amari != 0:
        ans += B[i] - amari

print(ans)
