N = int(input())
A = list(map(int, input().split()))

# 各桁に何個 1 があるかカウントできそう
#  1111111
#    11111
#      111
#       11

max_A = max(A)

# 階差で各桁の個数を計算
Counts = [0] * max_A

for a in A:
    Counts[a - 1] += 1


ans = []
digit_count = N
carry = 0
for i in range(len(Counts)):
    v = digit_count + carry

    first_digit = v % 10
    ans.append(str(first_digit))
    carry = v // 10

    digit_count -= Counts[i]

while carry > 0:
    ans.append(str(carry % 10))
    carry //= 10

print("".join(ans[::-1]))
