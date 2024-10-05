S = input()
T = input()


if S == T:
    print(0)
    exit()

long = min(len(S), len(T))

for i in range(long):
    if S[i] != T[i]:
        print(i + 1)
        exit()

if len(S) > len(T):
    print(len(T) + 1)
    exit()
elif len(S) < len(T):
    print(len(S) + 1)
    exit()
