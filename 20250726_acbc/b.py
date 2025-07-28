S = input()

T = ""

ready = True
for s in S:
    if s == "#":
        T += "#"
        ready = True
    else:
        if ready:
            T += "o"
            ready = False
        else:
            T += "."

print(T)
