N, A, B = map(int, input().split())

if B - A + 1 <= 0:
    print(0)
elif N == 1 and A != B:
    print(0)
elif N == 1 and A == B:
    print(1)
else:
    print((N - 2) * (B - A) + 1)
