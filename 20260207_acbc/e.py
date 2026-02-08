from sortedcontainers import SortedList

N, D = map(int, input().split())
A = list(map(int, input().split()))

s = SortedList([])
ans = 0
right = 0

for left in range(N):
    while right < N:
        # index
        index = s.bisect_left(A[right])
        if index - 1 >= 0 and abs(A[right] - s[index - 1]) < D:
            break
        if index < len(s) and abs(A[right] - s[index]) < D:
            break

        s.add(A[right])
        right += 1

    ans += right - left

    # leftを１進めるため、対象範囲から削除
    s.discard(A[left])

print(ans)
