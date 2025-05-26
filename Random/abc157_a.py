A = []

for _ in range(3):
    a = list(map(int, input().split()))
    A.append(a)

N = int(input())

called_number = set()

for _ in range(N):
    b = int(input())
    called_number.add(b)

ans = False

# rowチェック
for i in range(3):
    for j in range(3):
        if A[i][j] not in called_number:
            break
        if j == 2:
            ans = True

# colチェック
for i in range(3):
    for j in range(3):
        if A[j][i] not in called_number:
            break
        if j == 2:
            ans = True

# left to right cross check
for i in range(3):
    if A[i][i] not in called_number:
        break
    if i == 2:
        ans = True

# right to left cross check
for i in range(3):
    if A[i][2 - i] not in called_number:
        break
    if i == 2:
        ans = True

if ans:
    print("Yes")
else:
    print("No")
