a, b = map(int, input().split())


concat_num = int(str(a) + str(b))

doubles = set()

for i in range(1, 360):
    doubles.add(i**2)

if concat_num in doubles:
    print("Yes")
else:
    print("No")
