S = input()

d = {}

for s in S:
    d[s] = d.get(s, 0) + 1


if len(S) == 1:
    print("YES")
    exit()
elif len(S) == 2:
    if len(d.keys()) == 1:
        print("NO")
        exit()
    else:
        print("YES")
        exit()


temp = len(S) // 3
amari = len(S) % 3

if amari == 0:
    if d.get("a", 0) == temp and d.get("b", 0) == temp and d.get("c", 0) == temp:
        print("YES")
        exit()
    else:
        print("NO")
        exit()
else:
    if (
        abs(d.get("a", 0) - d.get("b", 0)) <= 1
        and abs(d.get("b", 0) - d.get("c", 0)) <= 1
        and abs(d.get("a", 0) - d.get("c", 0)) <= 1
    ):
        print("YES")
        exit()
    else:
        print("NO")
        exit()
