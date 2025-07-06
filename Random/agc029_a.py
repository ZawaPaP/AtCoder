S = input()

# n 番目の W が Sの index i に存在
# w_map[n - 1] = i
w_map = []

for i in range(len(S)):
    if S[i] == "W":
        w_map.append(i)

ans = 0
w_count = 0
for w in w_map:
    ans += w - w_count
    w_count += 1

print(ans)
