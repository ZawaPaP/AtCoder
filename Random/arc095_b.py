n = int(input())

A = list(map(int, input().split()))

A.sort()

Ai = A[-1]
Aj = A[0]

# Ai // 2に近い数をbinary searchで探す
temp = Ai
real_mid = Ai / 2
for i in range(n - 1):
    if abs(A[i] - real_mid) < temp:
        temp = abs(A[i] - real_mid)
        Aj = A[i]

print(Ai, Aj)
