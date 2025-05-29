S = input()

chars = set()

for c in S:
    if c in chars:
        print("no")
        exit()

    chars.add(c)

print("yes")
