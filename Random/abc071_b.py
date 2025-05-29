S = input()

for i in range(97, 123):
    if chr(i) in S:
        continue
    else:
        print(chr(i))
        exit()

print("None")
