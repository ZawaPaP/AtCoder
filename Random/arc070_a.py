X = int(input())

temp = 0
for i in range(abs(X) + 1):
    if temp + i >= abs(X):
        print(i)
        exit()
    temp += i
