A = list(map(int, input().split()))


one_c = 0
two_c = 0
three_c = 0
four_c = 0

for i in range(0, len(A)):
    if A[i] == 1:
        one_c += 1
    elif A[i] == 2:
        two_c += 1
    elif A[i] == 3:
        three_c += 1
    elif A[i] == 4:
        four_c += 1

sum = one_c // 2 + two_c // 2 + three_c // 2 + four_c // 2
print(int(sum))
