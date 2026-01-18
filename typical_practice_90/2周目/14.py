N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

dist = 0
for i in range(len(A)):
    dist += abs(A[i] - B[i])

print(dist)
