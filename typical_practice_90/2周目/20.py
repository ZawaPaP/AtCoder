import math

a, b, c = map(int, input().split())

x = 1
for _ in range(b):
    x *= c
    if x > a:
        print("Yes")
        exit()
print("No")
