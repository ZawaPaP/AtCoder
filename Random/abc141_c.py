N, K, Q = map(int, input().split())

A = {}
for _ in range(Q):
    a = int(input())
    if a in A:
        A[a] += 1
    else:
        A[a] = 1


for player_num in range(1, N + 1):
    point = A.get(player_num, 0) - Q

    if K + point > 0:
        print("Yes")
    else:
        print("No")
