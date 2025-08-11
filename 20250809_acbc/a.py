N = int(input())
S = input()

if N < 3:
    print("No")
    exit()

if S[-3:] == "tea":
    print("Yes")
else:
    print("No")
