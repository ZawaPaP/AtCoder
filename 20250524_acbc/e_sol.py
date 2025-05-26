from heapq import heappop, heappush

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    # 最大値を取り出すため、-1を掛けて最小ヒープを使う
    que = []

    for i in range(N):
        if i == 0:
            heappush(que, -A[0])  # 最初は1つだけ
        else:
            heappush(que, -A[2 * i - 1])  # 2つ追加
            heappush(que, -A[2 * i])

        ans += -heappop(que)  # 最大値を取り出して加算

    print(ans)
