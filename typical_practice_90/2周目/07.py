N = int(input())
A = list(map(int, input().split()))

Q = int(input())


# 常に探すと O(A x B)だが、sortすることで実質 O(max(A, B))となる
# sortの計算量に引っ張られるため、(O(NlogN))

A.sort()


def binary_search_nearest_idx(x):
    l, r = 0, N
    while l + 1 < r:
        mid = (l + r) // 2

        if A[mid] > x:
            r = mid
        else:
            l = mid
    return l


for _ in range(Q):
    b = int(input())

    if N == 1:
        print(abs(A[0] - b))
        continue

    idx = binary_search_nearest_idx(b)
    if idx == N - 1:
        print(abs(A[idx] - b))
    else:
        print(min(abs(A[idx] - b), abs(A[idx + 1] - b)))
