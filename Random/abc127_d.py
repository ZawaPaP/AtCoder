import heapq

N, M = map(int, input().split())

A = list(map(int, input().split()))

query = []

hq = []
for a in A:
    heapq.heappush(hq, a)

for _ in range(M):
    B, C = map(int, input().split())

    query.append((B, C))

query.sort(key=lambda x: x[1], reverse=True)

for B, C in query:
    for _ in range(B):
        top = heapq.heappop(hq)
        if top < C:
            heapq.heappush(hq, C)
        else:
            heapq.heappush(hq, top)
            break

print(sum(hq))
