import heapq

T = int(input())
ans = []
for _ in range(T):
    N, K, X = map(int, input().split())
    A = list((float(-1 * int(a)), 1) for a in input().split())

    heapq.heapify(A)

    while K > 0:
        l, c = heapq.heappop(A)
        if c <= K:
            K -= c
            heapq.heappush(A, (l / 2, c * 2))
        else:
            heapq.heappush(A, (l / 2, K * 2))
            heapq.heappush(A, (l, c - K))
            K = 0

    while X > 0:
        l, c = heapq.heappop(A)
        X -= c

    ans.append(l * -1)

for a in ans:
    print(a)
