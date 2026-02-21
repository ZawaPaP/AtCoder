N = int(input())
S = input()

s1 = set()
s2 = set()
s3 = set()

for char in S:
    for prev2 in s2:
        s3.add(prev2 + char)

    for prev1 in s1:
        s2.add(prev1 + char)

    s1.add(char)

print(len(s3))
