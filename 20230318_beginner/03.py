N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


ansA = []
ansB = []

cnt = 1
while len(A) > 0 and len(B) > 0:
    if A[0] > B[0]:
        B.pop(0)
        ansB.append(cnt)
        cnt += 1
    else:
        A.pop(0)
        ansA.append(cnt)
        cnt += 1

while len(A) > 0:
    A.pop(0)
    ansA.append(cnt)
    cnt += 1
while len(B) > 0:
    B.pop(0)
    ansB.append(cnt)
    cnt += 1

print(*ansA)
print(*ansB)