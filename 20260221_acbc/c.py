from collections import deque

T = int(input())

rems = []
for _ in range(T):
    n, d = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    queue = deque()
    for i in range(n):
        queue.append([A[i], i])
        amount = B[i]
        while queue and amount > 0:
            if queue[0][0] <= amount:
                amount -= queue.popleft()[0]
            else:
                queue[0][0] -= amount
                amount = 0

        while queue and queue[0][1] <= i - d:
            queue.popleft()

    rem = sum(q[0] for q in queue)
    rems.append(rem)

for r in rems:
    print(r)
