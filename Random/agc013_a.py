from enum import Enum

N = int(input())

A = list(map(int, input().split()))


class Delta(Enum):
    DEFAULT = 0
    UP = 1
    DOWN = 2


ans = 0
status = Delta.DEFAULT
for i in range(1, N):
    if A[i] > A[i - 1]:
        if status == Delta.DOWN:
            ans += 1
            status = Delta.DEFAULT
        else:
            status = Delta.UP

    elif A[i] < A[i - 1]:
        if status == Delta.UP:
            ans += 1
            status = Delta.DEFAULT
        else:
            status = Delta.DOWN

ans += 1
print(ans)
