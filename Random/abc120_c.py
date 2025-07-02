S = input()

zero_count = 0
one_count = 0

for s in S:
    if s == "0":
        zero_count += 1
    else:
        one_count += 1

print(min(one_count, zero_count) * 2)
