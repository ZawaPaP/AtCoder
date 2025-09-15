import heapq
from collections import deque

N, K = map(int, input().split())

customers_queue = deque()
exit_heap = []

for i in range(N):
    a, b, c = map(int, input().split())
    customers_queue.append((a, b, c))

enter_times = []
capacity = K

# 最初はcapacity分だけ入店
while customers_queue and customers_queue[0][2] <= capacity:
    a, b, c = customers_queue.popleft()
    enter_times.append(a)
    heapq.heappush(exit_heap, (a + b, c))
    capacity -= c

# その後は、退店を待って入店
while customers_queue:
    exit_time, c = heapq.heappop(exit_heap)
    capacity += c
    while customers_queue and customers_queue[0][2] <= capacity:
        a, b, c = customers_queue.popleft()
        enter_time = max(exit_time, a)
        enter_times.append(enter_time)
        heapq.heappush(exit_heap, (enter_time + b, c))
        capacity -= c

for i in range(N):
    print(enter_times[i])
