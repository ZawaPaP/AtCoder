N, L, R = map(int, input().split())

S = input()

for i in range(L, R + 1):
    if S[i - 1] == "x":
        print("No")
        exit()

print("Yes")
