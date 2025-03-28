N, M = map(int, input().split())

A_mod = []

temp = list(map(int, input().split()))
for i in range(0, N):
    A_mod.append(temp[i] % M)


count = 0
for j in range(N, 0, -1):
    # An_mod は最終的に [ (A(n) + A(n-1))mod, AN + A(n-1) + A(n-2)mod, ... , A(n) +  ] となる
    An_mod = []
    prev_mod = A_mod[j - 1]
    for i in range(j - 2, -1, -1):
        if (prev_mod + A_mod[i]) > M:
            An_mod.append(prev_mod + A_mod[i] - M)
            prev_mod = prev_mod + A_mod[i] - M
        else:
            An_mod.append(prev_mod + A_mod[i])
            prev_mod = prev_mod + A_mod[i]
    count += sum(An_mod)

count += sum(A_mod)
print(count)
