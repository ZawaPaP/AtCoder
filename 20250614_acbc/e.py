from functools import lru_cache

N, H, M = map(int, input().split())

Monsters = [list(map(int, input().split())) for _ in range(N)]


@lru_cache(maxsize=None)
def dfs(hitpoint, magic, i):
    if i == N:
        return i
    if hitpoint < Monsters[i][0] and magic < Monsters[i][1]:
        return i
    elif hitpoint < Monsters[i][0] and magic >= Monsters[i][1]:
        return dfs(hitpoint, magic - Monsters[i][1], i + 1)
    elif hitpoint >= Monsters[i][0] and magic < Monsters[i][1]:
        return dfs(hitpoint - Monsters[i][0], magic, i + 1)
    else:
        return max(
            dfs(hitpoint - Monsters[i][0], magic, i + 1),
            dfs(hitpoint, magic - Monsters[i][1], i + 1),
        )


print(dfs(H, M, 0))
