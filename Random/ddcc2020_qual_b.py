N = int(input())
A = list(map(int, input().split()))

# 累積和
cumsum = [0]
for a in A:
    cumsum.append(cumsum[-1] + a)

total = cumsum[-1]
min_diff = float("inf")

for i in range(1, N):
    left = cumsum[i]
    right = total - left
    diff = abs(left - right)
    min_diff = min(min_diff, diff)

print(min_diff)
