# この問題は一見、経路問題に見えますが、問題文をよく読むと
# 都市の数はN, 道の数は N - 1, そして全都市に道を通って移動可能。とあります。
# 上記条件から、同じ都市間を結ぶ道路は複数存在しないことがわかります。

# そのため、任意の都市からBFS or DFSを使い一番エッジとなる都市を求め、
# そのエッジから再度、一番遠い都市を求めると、最長距離がわかります。
# 実際には1本道路を追加するため、求める答えは上記の際長距離 + 1 となります。

N = int(input())

G = [[] for _ in range(N + 1)]


def get_farthest_node(start_node):

    distance = [-1] * (N + 1)
    distance[start_node] = 0
    stack = [start_node]

    while stack:
        current = stack.pop()
        for node in G[current]:
            if distance[node] == -1:
                stack.append(node)
                distance[node] = distance[current] + 1

    max_distance = max(distance)
    farthest_node = distance.index(max_distance)
    return max_distance, farthest_node


for i in range(N - 1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

# 1回目のdfsでエッジとなる都市を求める
_, farthest_node = get_farthest_node(1)

# 2回目のdfsでエッジからの距離を求める
max_distance, _ = get_farthest_node(farthest_node)

# 道を新設するため、 +1
print(max_distance + 1)
