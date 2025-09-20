a, b, c = map(int, input().split())

count = 0
if a == b:
    count += 1
if a == c:
    count += 1
if b == c:
    count += 1

if count >= 1:
    print("Yes")
else:
    print("No")
