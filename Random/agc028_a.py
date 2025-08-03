import math

N, M = map(int, input().split())

S = input()
T = input()

lcm = math.lcm(N, M)

L = {}

for i in range(N):
    L[i * (lcm // N)] = S[i]

for i in range(M):
    if i * (lcm // M) in L and L[i * (lcm // M)] != T[i]:
        print(-1)
        exit()

print(lcm)
