N, M = map(int, input().split())

A = [list(input()) for _ in range(N)]
B = [list(input()) for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        for k in range(M):
            for l in range(M):
                if A[i + k][j + l] != B[k][l]:
                    break
            # pythonのfor else構文
            # forループがbreakされなかった場合にelseが実行される
            else:
                continue
            break
        else:
            print("Yes")
            exit()

print("No")
