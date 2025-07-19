N, T = map(int, input().split())
t = list(map(int, input().split()))

total = 0
for i in range(1, N):
    total += min(t[i] - t[i - 1], T)

# 最後に押した時はT出る
total += T

print(total)
