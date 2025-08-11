N = int(input())

B = list(map(int, input().split()))

# 挿入手順を考えると、常にB[index] == (index + 1) が成立するindexが存在しないと成立しない
# そうならないように末尾側から、B[index] == (index + 1) の場合は、取り出していく

order = []
CONTINUE = True

while B and CONTINUE:
    CONTINUE = False
    for i in range(len(B) - 1, -1, -1):
        if B[i] == i + 1:
            order.append(B.pop(i))
            CONTINUE = True
            break

if len(order) != N:
    print(-1)
    exit()

for o in reversed(order):
    print(o)
