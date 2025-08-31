from collections import deque

Rt, Ct, Ra, Ca = map(int, input().split())
N, M, L = map(int, input().split())

S = deque()
T = deque()

for _ in range(M):
    s, a = input().split()
    S.append([int(a), s])

for _ in range(L):
    t, b = input().split()
    T.append([int(b), t])


def calc(takahashi_position, aoki_position, dt, da, steps):
    if da == dt:
        if takahashi_position == aoki_position:
            return ('ALWAYS', steps)
        else:
            return ('NEVER', 0)
    else:
        shou = (takahashi_position - aoki_position) / (da - dt)
        if shou.is_integer() and shou > 0 and shou <= steps:
            return ('ONCE', shou)
        else:
            return ('NEVER', 0)


takahashi_h = Rt
takahashi_w = Ct
aoki_h = Ra
aoki_w = Ca

s_query = S.popleft()
t_query = T.popleft()
ans = 0

while S or T or s_query[0] > 0 or t_query[0] > 0:
    if s_query[0] == 0 and S:
        s_query = S.popleft()
    if t_query[0] == 0 and T:
        t_query = T.popleft()

    moves = min(s_query[0], t_query[0])
    s_query[0] -= moves
    t_query[0] -= moves

    # 移動方向による変化量を計算
    dh_t = dw_t = dh_a = dw_a = 0

    if s_query[1] == 'U':
        dh_t = -1
    elif s_query[1] == 'D':
        dh_t = 1
    elif s_query[1] == 'L':
        dw_t = -1
    elif s_query[1] == 'R':
        dw_t = 1

    if t_query[1] == 'U':
        dh_a = -1
    elif t_query[1] == 'D':
        dh_a = 1
    elif t_query[1] == 'L':
        dw_a = -1
    elif t_query[1] == 'R':
        dw_a = 1

    # ここで、
    # takahashi_h + x * dh_t = aoki_h + x * dh_a
    # takahashi_w + x * dw_t = aoki_w + x * dw_a
    # を満たす整数xが moves以下で存在するかを確認

    h_calc = calc(takahashi_h, aoki_h, dh_t, dh_a, moves)
    w_calc = calc(takahashi_w, aoki_w, dw_t, dw_a, moves)

    if h_calc[0] == 'ALWAYS' and w_calc[0] == 'ALWAYS':
        ans += moves
    elif h_calc[0] == 'ALWAYS' and w_calc[0] == 'ONCE':
        ans += 1
    elif w_calc[0] == 'ALWAYS' and h_calc[0] == 'ONCE':
        ans += 1
    elif h_calc[0] == 'ONCE' and w_calc[0] == 'ONCE':
        if h_calc[1] == w_calc[1]:
            ans += 1
    else:
        ans += 0

    takahashi_h += dh_t * moves
    takahashi_w += dw_t * moves
    aoki_h += dh_a * moves
    aoki_w += dw_a * moves

print(ans)
