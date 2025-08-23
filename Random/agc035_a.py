N = int(input())

A = list(map(int, input().split()))

caps = {}
for a in A:
    caps[a] = caps.get(a, 0) + 1

if len(caps) == 1 and 0 in caps:
    print("Yes")
    exit()

if len(caps) == 2:
    if 0 in caps and caps[0] == N / 3:
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if len(caps) == 3:
    xor = 0
    for k, v in caps.items():
        xor ^= k
        if v != N / 3:
            print("No")
            exit()

    if xor == 0:
        print("Yes")
        exit()
    else:
        print("No")
        exit()
print("No")
