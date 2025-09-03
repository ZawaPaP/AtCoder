N = int(input())
A = list(map(int, input().split()))

negatives = []
positives = []

for a in A:
    if a < 0:
        negatives.append(a)
    else:
        positives.append(a)

negatives.sort(reverse=True)
positives.sort()

if (len(negatives) == 0 or len(negatives) % 2 == 0):
    print(sum(positives) + abs(sum(negatives)))
    exit()

else:
    abs_min = min(abs(negatives[0]), positives[0]
                  if len(positives) > 0 else float("inf"))
    print(sum(positives) + abs(sum(negatives)) - 2 * abs_min)
