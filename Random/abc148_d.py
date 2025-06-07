N = int(input())
A = list(map(int, input().split()))

ans = -1

correct_brick = 0
brick_index = 1

for a in A:
    if a == brick_index:
        correct_brick += 1
        brick_index += 1

if correct_brick == 0:
    print(-1)
else:
    print(len(A) - correct_brick)
