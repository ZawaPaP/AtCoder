S = input()

st = set(S)

for i in range(97, 123):
    if chr(i) not in st:
        print(chr(i))
        exit()
