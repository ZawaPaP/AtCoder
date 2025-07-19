s = input()
t = input()

s = sorted(s)
t = sorted(t, reverse=True)

shortest = min(len(s), len(t))

for i in range(shortest):
    if s[i] > t[i]:
        print("No")
        exit()
    elif s[i] < t[i]:
        print("Yes")
        exit()

if len(s) >= len(t):
    print("No")
else:
    print("Yes")
