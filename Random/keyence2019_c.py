
N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if sum(A) < sum(B):
    print(-1)
    exit()


negative_diffs = []
positive_diffs = []

for i in range(N):
    diff = A[i] - B[i]
    if diff < 0:
        negative_diffs.append(diff)
    else:
        positive_diffs.append(diff)

negative_diffs.sort(reverse=True)
positive_diffs.sort(reverse=True)

count = len(negative_diffs)
negative_sum = sum(negative_diffs)

for positive_diff in positive_diffs:
    if negative_sum >= 0:
        break
    negative_sum += positive_diff
    count += 1

print(count)
