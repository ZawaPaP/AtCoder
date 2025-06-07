S = input()


if S[0] != "A":
    print("WA")
    exit()

s = S[2:-1]
c_count = 0
c_index = 2
for i, char in enumerate(s):
    if char == "C":
        c_count += 1
        c_index += i

if c_count != 1:
    print("WA")
    exit()

for i in range(len(S)):
    if i == 0 or i == c_index:
        continue

    if S[i].islower():
        continue
    else:
        print("WA")
        exit()

print("AC")
