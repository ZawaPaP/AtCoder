N, M = map(int, input().split())

S = [list(input()) for _ in range(N)]

votes = []


for i in range(M):
    zero_count = 0
    one_count = 0
    for s in S:
        if s[i] == "0":
            zero_count += 1
        else:
            one_count += 1

    votes.append((zero_count, one_count))

scores = [0] * N
for i in range(M):
    x = votes[i][0]
    y = votes[i][1]
    if x == 0 or y == 0:
        for j in range(N):
            scores[j] += 1
    elif x < y:
        for j in range(N):
            if S[j][i] == "0":
                scores[j] += 1
    else:
        for j in range(N):
            if S[j][i] == "1":
                scores[j] += 1

m_score = max(scores)

winners = []
for i in range(N):
    if scores[i] == m_score:
        winners.append(i + 1)

print(*winners)
