from collections import deque


N, Q = map(int, input().split())

event = [None] * Q

for i in range(Q):
    event[i] = list(map(int, input().split()))

q = deque()
called = set()
ans = []
cnt = 1
for i in range(Q):
    if event[i][0] == 1:
        q.append(cnt)
        cnt += 1
    elif event[i][0] == 2:
        called.add(event[i][1])
    else:
        while q:
            if q[0] not in called:
                ans.append(q[0])
                break
            else:
                q.popleft()

print(*ans)