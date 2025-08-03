N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]

T.sort()

wait = 0
passengers = 1
busses = 1
for i in range(1, N):
    next_time = T[i] - T[i - 1]

    if wait + next_time > K or passengers == C:
        wait = 0
        busses += 1
        passengers = 1
    else:
        wait += next_time
        passengers += 1

print(busses)
