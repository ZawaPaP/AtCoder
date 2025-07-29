N = int(input())
X = list(map(int, input().split()))

sorted_X = sorted(X)

mid_l = sorted_X[N // 2 - 1]
mid_r = sorted_X[N // 2]

for i in range(N):
    if X[i] <= mid_l:
        print(mid_r)
    else:
        print(mid_l)
