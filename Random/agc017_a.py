N, P = map(int, input().split())

A = list(map(int, input().split()))

d = {}

for a in A:
    if a % 2 == 0:
        d["e"] = d.get("e", 0) + 1
    else:
        d["o"] = d.get("o", 0) + 1


if d.get("o", 0) == 0 and P == 0:
    print(2**N)
    exit()
elif d.get("o", 0) == 0 and P == 1:
    print(0)
    exit()
else:
    print(2 ** (N - 1))
