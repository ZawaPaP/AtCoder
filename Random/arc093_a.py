N = int(input())
A = list(map(int, input().split()))

base_cost = 0
current_idx = 0
for a in A:
    base_cost += abs(a - current_idx)
    current_idx = a
# 最後0に戻る
base_cost += abs(current_idx)


A.insert(0, 0)
A.append(0)

for i in range(1, N + 1):
    if A[i - 1] < A[i] < A[i + 1]:
        print(base_cost)
    elif A[i - 1] > A[i] > A[i + 1]:
        print(base_cost)
    else:
        cost = base_cost - abs(A[i] - A[i - 1]) - abs(A[i + 1] - A[i])
        cost += abs(A[i + 1] - A[i - 1])
        print(cost)
