A, B, C = map(int, input().split())

if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
    print(0)
    exit()

lst = [A, B, C]
lst.sort()

print(lst[0] * lst[1])
