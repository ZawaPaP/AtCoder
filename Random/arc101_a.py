N, K = map(int, input().split())

X = list(map(int, input().split()))

negatives = [0]
positives = [0]

for x in X:
    if x < 0:
        negatives.append(-x)
    else:
        positives.append(x)

negatives.sort()

# 最初負に i 進み、その後、正に K - i 進むコストを計算

ans = float("inf")

for i in range(len(negatives)):
    j = K - i
    if 0 <= j < len(positives):
        ans = min(ans, abs(negatives[i]) * 2 + abs(positives[j]))

# 最初正に i 進み、その後、負に K - i 進むコストを計算

for i in range(len(positives)):
    j = K - i
    if 0 <= j < len(negatives):
        ans = min(ans, abs(positives[i]) * 2 + abs(negatives[j]))

print(ans)
