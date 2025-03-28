N, K = map(int, input().split())
S = list(input())

strawberry = 0
count = 0
for i in range(len(S)):
    if S[i] == "O":
        count += 1
    else:
        count = 0

    if count >= K:
        strawberry += 1
        count = 0

print(strawberry)
