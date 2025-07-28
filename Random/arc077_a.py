n = int(input())

A = list(map(int, input().split()))

b = []

for i in range(n):
    if i % 2 != 0:
        b.append(A[i])
    else:
        b.insert(0, A[i])

if n % 2 == 0:
    b.reverse()

print(*b)
