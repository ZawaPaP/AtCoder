N, M, Q = map(int, input().split())

dic = {i: set() for i in range(1, N + 1)}

all_set = {i for i in range(1, M + 1)}

ans = []

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        dic[query[1]].add(query[2])
    if query[0] == 2:
        dic[query[1]] = all_set
    if query[0] == 3:
        if query[2] in dic[query[1]]:
            ans.append("Yes")
        else:
            ans.append("No")


for answer in ans:
    print(answer)
