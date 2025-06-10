N, K = map(int, input().split())

H = [int(input()) for _ in range(N)]

H.sort()

left_p = 0
right_p = K - 1

min_diff = float("inf")

while right_p < N:
    min_diff = min(min_diff, H[right_p] - H[left_p])
    left_p += 1
    right_p += 1


print(min_diff)
