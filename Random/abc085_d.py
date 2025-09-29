N, H = map(int, input().split())

A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

max_a = max(A)

# max_a より大きいb を持つ刀は全て最終的に投げる
# 大きい順に投げて、Hを超えたら終了
# 残った値を max_a の刀で斬る

B.sort(reverse=True)
ans = 0
for b in B:
    if b > max_a:
        H -= b
        ans += 1
        if H <= 0:
            print(ans)
            exit()

if H % max_a == 0:
    print(ans + H // max_a)
else:
    print(ans + H // max_a + 1)
