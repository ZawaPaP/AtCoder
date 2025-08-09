N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


min_capacity = min(A, B, C, D, E)

bottleneck = N // min_capacity

if bottleneck * min_capacity < N:
    bottleneck += 1

print(bottleneck + 4)
