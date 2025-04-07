def get_near_index(numbers, value) -> int:
    left = 0
    right = len(numbers) - 1

    while left <= right:

        # left == right の時、nearest_index
        if left == right:
            return left

        mid = (left + right) // 2

        if value == numbers[mid]:
            return mid
        elif value < numbers[mid]:
            right = mid - 1
        elif value > numbers[mid]:
            left = mid + 1
    # left > right の時、midがnear_index
    return mid


N = int(input())

A = list(map(int, input().split()))

len_A = len(A)

A.sort()

Q = int(input())
for _ in range(Q):
    B = int(input())
    if len_A == 1:
        print(abs(A[0] - B))
        continue
    index = get_near_index(A, B)

    if index == 0:
        print(min(abs(A[index] - B), abs(A[index + 1] - B)))
        continue
    elif index == len_A - 1:
        print(min(abs(A[index] - B), abs(A[index - 1] - B)))
    else:
        print(min(min(abs(A[index] - B), abs(A[index - 1] - B)), abs(A[index + 1] - B)))
