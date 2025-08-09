N, M = map(int, input().split())

expected_try = 1 / (0.5 ** M)

one_try_time = M * 1900 + (N - M) * 100

print(int(expected_try * one_try_time))
