K, N = map(int, input().split())
A = list(map(int, input().split()))

longest_distance = (K - A[-1]) + A[0]

prev_pos = 0
for a in A:
    longest_distance = max(longest_distance, a - prev_pos)
    prev_pos = a

print(K - longest_distance)
