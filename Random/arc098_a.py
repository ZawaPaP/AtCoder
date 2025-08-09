N = int(input())
S = input()

w_and_e = []

left_east_count = 0
right_west_count = 0

for i in range(1, N):
    if S[i] == 'W':
        right_west_count += 1

w_and_e.append((left_east_count, right_west_count))

for i in range(1, N):
    prev = w_and_e[i - 1]
    east_c = prev[0]
    west_c = prev[1]
    if S[i - 1] == 'E':
        east_c += 1
    if S[i] == 'W':
        west_c -= 1
    w_and_e.append((east_c, west_c))

ans = float('inf')
for i in range(N):
    ans = min(ans, N - (w_and_e[i][0] + w_and_e[i][1]) - 1)

print(ans)
