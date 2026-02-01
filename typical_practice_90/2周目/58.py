N, K = map(int, input().split())


def get_digit_sum(x):
    return (x + sum(map(int, list(str(x))))) % 10**5


visited = [-1] * (10**5)
history = []

tmp = N
for i in range(K):
    if visited[tmp] != -1:
        loop_start_step = visited[tmp]
        loop_len = i - loop_start_step

        rem_k = (K - i) % loop_len
        ans = history[loop_start_step + rem_k]
        print(ans)
        exit()

    visited[tmp] = i
    history.append(tmp)
    tmp = get_digit_sum(tmp)

print(tmp)
