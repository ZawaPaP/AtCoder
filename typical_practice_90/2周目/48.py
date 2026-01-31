import heapq

N, K = map(int, input().split())

# scoresには (B, A) tupleが入る
scores = []
for _ in range(N):
    a, b = map(int, input().split())
    # pythonは min heapのため符号逆転
    scores.append((-b, a))


heapq.heapify(scores)

ans = 0
while K > 0 and len(scores) > 0:
    curr = heapq.heappop(scores)
    ans += -1 * curr[0]
    # a - bのscoreを入れておく
    rem = curr[1] + curr[0]
    heapq.heappush(scores, (-rem, rem))
    K -= 1

print(ans)
