N = int(input())

A = list(int(input()) for _ in range(N))

sorted_A = sorted(A, reverse=True)

max_num = sorted_A[0]
second_num = sorted_A[1]

for num in A:
    if num == max_num:
        print(second_num)
    else:
        print(max_num)
