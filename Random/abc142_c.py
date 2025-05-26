N = int(input())

A = list(map(int, input().split()))

Ans = [0] * N

for i, a in enumerate(A):
    Ans[a - 1] = str(i + 1)


print(" ".join(Ans))
