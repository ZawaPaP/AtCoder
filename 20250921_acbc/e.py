import heapq

T = int(input())
ans = []
for _ in range(T):
    N, K, X = map(int, input().split())
    A = [-1 * a for a in list(map(float, input().split()))]
    heapq.heapify(A)
    while K > 0:
        a = heapq.heappop(A)
        heapq.heappush(A, a / 2)
        heapq.heappush(A, a / 2)
        K -= 1
    while X > 0:
        heapq.heappop(A)
        X -= 1
    ans.append(heapq.heappop(A))

for a in ans:
    print(a * -1)
