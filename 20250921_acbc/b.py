N, M, K = map(int, input().split())

events = [[0 for _ in range(M)] for _ in range(N)]

ans = []


def check_event(events):
    for i, ppl in enumerate(events):
        if sum(ppl) == M and i + 1 not in ans:
            ans.append(i + 1)


for _ in range(K):
    a, b = map(int, input().split())
    events[a - 1][b - 1] = 1
    check_event(events)

print(*ans)
