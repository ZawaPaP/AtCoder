import itertools
import math

N = int(input())

towns = []

for _ in range(N):
    x, y = map(int, input().split())
    towns.append((x, y))

distances = []

for permutation in itertools.permutations(range(0, N)):
    distance = 0
    for i in range(1, len(permutation)):
        prev_idx = permutation[i - 1]
        next_idx = permutation[i]
        distance += math.sqrt(
            (towns[next_idx][0] - towns[prev_idx][0]) ** 2
            + (towns[next_idx][1] - towns[prev_idx][1]) ** 2
        )
    distances.append(distance)


print(sum(distances) / len(distances))
