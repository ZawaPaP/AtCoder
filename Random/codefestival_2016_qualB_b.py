N, A, B = map(int, input().split())
S = input()

passed = 0
from_abroad = 0

for s in S:
    if s == "a":
        if passed < A + B:
            print("Yes")
            passed += 1
            continue
    if s == "b":
        if passed < A + B and from_abroad < B:
            print("Yes")
            passed += 1
            from_abroad += 1
            continue
    print("No")
