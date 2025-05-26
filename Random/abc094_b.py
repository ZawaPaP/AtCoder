N, M, X = map(int, input().split())

A = list(map(int, input().split()))


cost_gate = set(A)

ans_to_x = 0
for i in range(X, N):
    if i in cost_gate:
        ans_to_x += 1

ans_to_zero = 0
for i in range(0, X):
    if i in cost_gate:
        ans_to_zero += 1

print(min(ans_to_zero, ans_to_x))
