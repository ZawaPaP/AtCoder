N = int(input())

S = input()

# Aを偶数index 0, 2, 4, ... に入れるのにかかるコスト

even_need_to_move_A = []
odd_need_to_move_A = []
even_need_to_move_B = []
odd_need_to_move_B = []

even_cost = 0
odd_cost = 0

for i in range(2 * N):
    if S[i] == 'A':
        if i % 2 == 0:
            even_need_to_move_A.append(i)
        else:
            odd_need_to_move_A.append(i)
    if S[i] == 'B':
        if i % 2 != 0:
            even_need_to_move_B.append(i)
        else:
            odd_need_to_move_B.append(i)


for i in range(len(even_need_to_move_A)):
    even_cost += abs(even_need_to_move_A[i] - even_need_to_move_B[i])

for i in range(len(odd_need_to_move_A)):
    odd_cost += abs(odd_need_to_move_A[i] - odd_need_to_move_B[i])

print(min(even_cost, odd_cost))
