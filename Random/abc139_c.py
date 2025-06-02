N = int(input())

H = list(map(int, input().split()))

Count = [0] * N

count = 0
for i in reversed(range(N - 1)):
    if H[i] >= H[i + 1]:
        count += 1
    else:
        count = 0
    Count[i] = count

print(max(Count))
