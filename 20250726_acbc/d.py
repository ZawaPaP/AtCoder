T = int(input())

ans = []

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort()

    temp = 0
    i, j = 0, 0
    while i < N and j < N:
        if A[i] + B[j] >= M:
            temp += (A[i] + B[j]) % M
            i += 1
            j += 1
        else:
            temp += B[j]
            j += 1

    while i < N:
        temp += A[i]
        i += 1

    ans.append(temp)

for a in ans:
    print(a)
