temp = input()

A = int(temp[0])
B = int(temp[1])
C = int(temp[2])
D = int(temp[3])

opes = ["+", "-"]

for i in range(2):
    for j in range(2):
        for k in range(2):
            total = A
            if i == 0:
                total += B
            else:
                total -= B

            if j == 0:
                total += C
            else:
                total -= C

            if k == 0:
                total += D
            else:
                total -= D

            if total == 7:
                ans = (
                    str(A)
                    + opes[i]
                    + str(B)
                    + opes[j]
                    + str(C)
                    + opes[k]
                    + str(D)
                    + "=7"
                )
                print(ans)
                exit()
