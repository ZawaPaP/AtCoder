import itertools

N = int(input())

S = list(input())

next_pos = [[-1] * 10 for _ in range(N)]


for i in range(N - 1, -1, -1):
    for c in range(10):
        if i < N and S[i] == str(c):
            next_pos[i][c] = i
        else:
            next_pos[i][c] = next_pos[i + 1][c] if i < N - 1 else -1

# next_pos[i][c] は i 以降で c が次に出てくる位置

ans = 0

for i in range(1000):
    target = f"{i:03d}"

    pos = 0

    for c in target:
        if pos < N:
            pos = next_pos[pos][int(c)]
            if pos == -1:
                break
            pos += 1
        else:
            break
    else:
        ans += 1

print(ans)
