N, M, C = map(int, input().split())
B = list(map(int, input().split()))

ans = 0


def check(A, B, C):
    temp = 0
    for i in range(M):
        temp += A[i] * B[i]
    return temp > -C


for _ in range(N):
    A = list(map(int, input().split()))

    if check(A, B, C):
        ans += 1

print(ans)
