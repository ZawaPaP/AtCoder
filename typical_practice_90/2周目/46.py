N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

a_counts = [0] * 46
b_counts = [0] * 46
c_counts = [0] * 46

for i in range(N):
    a = A[i] % 46
    b = B[i] % 46
    c = C[i] % 46
    a_counts[a] += 1
    b_counts[b] += 1
    c_counts[c] += 1

ans = 0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i + j + k) % 46 == 0:
                ans += a_counts[i] * b_counts[j] * c_counts[k]

print(ans)
