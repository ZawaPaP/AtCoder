N = int(input())
A = list(map(int, input().split()))

A.sort()

sum_a = sum(A)
sum_a -= A[-1]

# 一番大きいA[-1]は必ず答えとなる
ans = 1
for i in reversed(range(N - 1)):
    if sum_a * 2 >= A[i + 1]:
        ans += 1
        sum_a -= A[i]
    else:
        break

print(ans)
