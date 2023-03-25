#unsolved

#Points
#

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

s = set()
ans = 0

def dfs(i, j, s):
    global ans
    if A[i][j] in s:
        return
    if i == (H - 1) and j == (W - 1):
        ans += 1
        return
    s.add(A[i][j])
    if j + 1 < W:
        dfs(i, j + 1, s)
    if i + 1 < H:
        dfs(i + 1, j, s)
    s.remove(A[i][j])   #ここのsを消す考え方がわからなかった

dfs(0, 0, s)
print(ans)