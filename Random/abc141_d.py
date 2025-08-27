import heapq

N, M = map(int, input().split())

A = list(map(int, input().split()))

pq = []
for a in A:
    heapq.heappush(pq, -a)


for _ in range(M):
    top = heapq.heappop(pq)
    heapq.heappush(pq, (top + 1) // 2)

print(-sum(pq))