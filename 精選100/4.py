N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# i曲めとj曲めを歌うとしてscore 計算
score = 0
for i in range(M - 1):
    for j in range(i + 1, M):
        temp = 0
        for k in range(N):
            temp += max(A[k][i], A[k][j])
        score = max(score, temp)
print(score)
