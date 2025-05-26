N = int(input())

X = list(map(int, input().split()))

sum_x = sum(X)
abs_1 = sum(X) / len(X)
abs_int_1 = sum(X) // len(X)
abs_int_2 = abs_int_1 + 1 if abs_1 >= 0 else abs_int_1 - 1

if abs(abs_1 - abs_int_1) >= abs(abs_1 - abs_int_2):
    point = abs_int_2
else:
    point = abs_int_1

ans = 0
for x in X:
    ans += (x - point) ** 2

print(ans)
