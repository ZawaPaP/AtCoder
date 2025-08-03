S = input()
Q = int(input())

head = ""
tail = ""

reversed_flag = False

for _ in range(Q):
    query = input().split()
    t = query[0]
    if t == "1":
        reversed_flag = not reversed_flag
    else:
        f = query[1]
        c = query[2]
        if f == "1":
            if reversed_flag:
                tail += c
            else:
                head = c + head
        else:
            if reversed_flag:
                head = c + head
            else:
                tail += c

if reversed_flag:
    print(tail[::-1] + S[::-1] + head[::-1])
else:
    print(head + S + tail)
