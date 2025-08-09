S = list(input())
K = int(input())


if len(S) == 1:
    if K == 1:
        print(0)
        exit()
    else:
        print(K // 2)
        exit()

# Sが一文字からなる場合
if len(set(S)) == 1:
    print(len(S) * K // 2)
    exit()

count = 0
c_S = S.copy()
for i in range(1, len(c_S)):
    if c_S[i] == c_S[i - 1]:
        c_S[i] = "*"
        count += 1
if S[0] != S[-1]:
    print(count * K)
    exit()


# 先頭の同じ文字の数
head_count = 1
# 末尾の同じ文字の数
tail_count = 1

for i in range(1, len(S)):
    if S[i] == S[0]:
        head_count += 1
    else:
        break

for i in range(len(S) - 2, -1, -1):
    if S[i] == S[-1]:
        tail_count += 1
    else:
        break

# 接続部での追加変更数
connected = (head_count + tail_count) // 2 - head_count // 2 - tail_count // 2
connected *= (K - 1)

print(count * K + connected)
