N = int(input())
S = input()

cnt = 0
for i in range(0, N - 2):
    if S[i] == ".":
        continue
    else:
        if S[i + 1] == ".":
            if S[i + 2] == "#":
                cnt += 1
print(cnt)
