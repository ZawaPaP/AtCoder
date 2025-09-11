K, T = map(int, input().split())

A = list(map(int, input().split()))

max_cake = max(A)

if (K + 1) // 2 >= max_cake:
    print(0)
else:
    print(K - (K - max_cake) * 2 - 1)
