T = int(input())


def get_reachables(start, S):
    r, c = start[0] - 1, start[1] - 1
    # 各列の「一番下の壁」の位置を記録
    bottom = [-1] * N
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#":
                bottom[j] = i

    # dp[c]: 現在の行の列cに到達可能
    dp = [[0] * N for _ in range(N)]
    for i in range(N):
        dp[i][c] = 1

        # 下の行から上の行へ
        for i in range(N - 2, -1, -1):
            for j in range(N):
                # すでに到達可能（スタート列や連鎖破壊済み）ならスキップ
                if dp[i][j]:
                    continue

                # 周囲（左下、真下、右下）のチェック
                ok = False
                if dp[i + 1][j]:
                    ok = True
                if j > 0 and dp[i + 1][j - 1]:
                    ok = True
                if j + 1 < N and dp[i + 1][j + 1]:
                    ok = True

                if ok:
                    if S[i][j] == ".":
                        dp[i][j] = 1
                    elif bottom[j] == i:
                        # ★重要：一番下の壁を壊せたら、その列の上の壁はすべて壊せる！
                        for k in range(i + 1):
                            dp[k][j] = 1

    return dp[0]


for _ in range(T):
    N, C = map(int, input().split())
    S = [list(input()) for _ in range(N)]
    ans = get_reachables((N, C), S)
    print("".join(map(str, ans)))
