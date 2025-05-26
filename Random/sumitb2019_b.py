import math

N = int(input())


for n in range(1, N + 1):
    if math.floor(n * 1.08) == N:
        print(n)
        exit()

print(":(")
