N, L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

A.append(L)


def able_to_separate(n):
    cnt = 0
    temp = A[0]
    for i in range(1, len(A)):
        if temp >= n:
            temp = 0
            cnt += 1
        temp += A[i] - A[i - 1]
    if temp >= n:
        cnt += 1
    return cnt >= K + 1


# 2分探索で最も短いものの長さを求める
l, r = 0, L
while l <= r:
    mid = (l + r) // 2
    if not able_to_separate(mid):
        r = mid - 1
    else:
        l = mid + 1

print(l - 1)
