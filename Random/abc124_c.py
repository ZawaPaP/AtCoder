S = input()

prev = S[0]
count = 0
for i in range(1, len(S)):
    if S[i] == prev:
        count += 1
        prev = "0" if S[i] == "1" else "1"
    else:
        prev = S[i]

print(count)
