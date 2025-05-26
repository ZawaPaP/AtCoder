A, B, C = map(int, input().split())

if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
    print(0)
    exit()

if A == B and B == C:
    print(-1)
    exit()


num_changes = 0

while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:

    temp_A = B // 2 + C // 2
    temp_B = A // 2 + C // 2
    temp_C = A // 2 + B // 2

    A = temp_A
    B = temp_B
    C = temp_C

    num_changes += 1

print(num_changes)
