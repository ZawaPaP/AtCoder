N, Q = map(int, input().split())

Queries = [input().split() for _ in range(Q)]

A = [i for i in range(1, N + 1)]
offset = 0  # 配列の開始位置を管理

for query in Queries:
    if query[0] == "1":
        pos = (int(query[1]) - 1 + offset) % N
        A[pos] = int(query[2])
    elif query[0] == "2":
        pos = (int(query[1]) - 1 + offset) % N
        print(A[pos])
    else:
        k = int(query[1])
        offset = (offset + k) % N
