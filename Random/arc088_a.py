X, Y = map(int, input().split())


ans = []

temp = X
while temp <= Y:
    ans.append(temp)
    temp *= 2

print(len(ans))
