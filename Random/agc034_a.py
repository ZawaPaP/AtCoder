N, A, B, C, D = map(int, input().split())

S = list(input())
S.insert(0, "S")

start = min(A, B)
end = max(C, D)

for i in range(start, min(len(S), end + 1)):
    if S[i - 1] == "#" and S[i] == "#":
        print("No")
        exit()

if A < B and C > D:
    for i in range(B, D + 1):
        if S[i - 1] == "." and S[i] == "." and S[i + 1] == ".":
            print("Yes")
            exit()
    print("No")
else:
    print("Yes")
