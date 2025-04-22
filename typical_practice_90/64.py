N, Q = map(int, input().split())

A = list(map(int, input().split()))

efforts = [0]

total_effort = 0

for i in range(1, len(A)):
    efforts.append(A[i] - A[i - 1])
    total_effort += abs(A[i] - A[i - 1])
# effortsには、各区間の移動の不便さが入る。
# 例えば、区画 1 - 2 間の不便さはefforts[1]

changes = []

for _ in range(Q):
    changes.append(list(map(int, input().split())))

for change in changes:
    L, R, V = change
    # L, R = 2, 3だとすると不便さは L - 1, L間と R, R + 1間で変動する
    if L > 1:
        new_effort = efforts[L - 1] + V
        total_effort -= abs(efforts[L - 1])
        total_effort += abs(new_effort)
        efforts[L - 1] += V
    if R < N:
        new_effort = efforts[R] - V
        total_effort -= abs(efforts[R])
        total_effort += abs(new_effort)
        efforts[R] -= V

    print(total_effort)
