T = list(input())

U = list(input())

left = 0
right = len(U) - 1


def check(left, right, T, U):
    for i, char in enumerate(U):
        if char == T[left + i] or T[left + i] == "?":
            continue
        else:
            return False
    return True


while right < len(T):
    if check(left, right, T, U):
        print("Yes")
        exit()

    left += 1
    right += 1


print("No")
