X, Y, N = map(int, input().split())

ans = []
for _ in range(N):
    u, v = map(int, input().split())
    # uの腕
    u_arm = (u - 1) // Y
    v_arm = (v - 1) // Y

    if u_arm == v_arm:
        ans.append(abs(u - v))
    else:
        # uの位置から0を通ってvの位置までの距離
        u_to_0 = (u - 1) % Y + 1 if u != 0 else 0
        v_to_0 = (v - 1) % Y + 1 if v != 0 else 0
        ans.append(u_to_0 + v_to_0)

for a in ans:
    print(a)
