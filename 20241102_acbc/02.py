N = int(input())

my_dict = {}

for i in range(1, N + 1):
    q, r = map(int, input().split())
    my_dict[i] = [q, r]

Q = int(input())

for i in range(0, Q):
    t, d = map(int, input().split())

    Q = my_dict[t][0]
    R = my_dict[t][1]

    temp = d
    if temp % Q == R:
        print(temp)

    elif temp % Q < R:
        print(temp + (R - temp % Q))
    else:
        print(temp + (Q - temp % Q) + R)
