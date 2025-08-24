N, Q = map(int, input().split())

A = list(map(int, input().split()))

B = list(map(int, input().split()))

base = []
for i in range(N):
    base.append(min(A[i], B[i]))

base_sum = sum(base)

for _ in range(Q):
    c, x, v = input().split()
    x = int(x)
    v = int(v)

    if c == 'A':
        A[x - 1] = v
        temp = min(A[x - 1], B[x - 1])
        base_sum -= base[x - 1]
        base_sum += temp
        base[x - 1] = temp
    else:
        B[x - 1] = v
        temp = min(A[x - 1], B[x - 1])
        base_sum -= base[x - 1]
        base_sum += temp
        base[x - 1] = temp

    print(base_sum)
