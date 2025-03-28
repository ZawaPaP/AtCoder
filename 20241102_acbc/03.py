N = int(input())
A = list(map(int, input().split()))

my_dict = {}
B = []

for i in range(1, N + 1):

    if A[i - 1] not in my_dict:
        my_dict[A[i - 1]] = i
        B.append(-1)
    else:
        B.append(my_dict[A[i - 1]])
        my_dict[A[i - 1]] = i

print(" ".join([str(b) for b in B]))
