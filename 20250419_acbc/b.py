Q = int(input())

queue = []

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        queue.append(query[1])
    else:
        num = queue.pop(0)
        print(num)
