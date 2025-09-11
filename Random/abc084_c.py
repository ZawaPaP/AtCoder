N = int(input())

times = []

for _ in range(N - 1):
    c, s, f = map(int, input().split())
    times.append((c, s, f))


for j in range(N - 1):
    spent_times = [0] * (N)
    for i in range(j, N - 1):
        c, s, f = times[i]
        if spent_times[i] < s:
            spent_times[i + 1] = s + c
        else:
            wait_time = 0 if spent_times[i] % f == 0 else f - \
                (spent_times[i] % f)
            spent_times[i + 1] = spent_times[i] + wait_time + c
    print(spent_times[-1])

print(0)
