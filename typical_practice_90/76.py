N = int(input())

A = list(map(int, input().split()))

sum_A = sum(A)

if sum_A % 10 != 0:
    print("No")
    exit()

expected = sum_A // 10

# 配列を2倍に拡張して循環を処理
A_extended = A + A

left = 0
right = 0
current_sum = 0

while right < 2 * N:
    current_sum += A_extended[right]
    right += 1

    while current_sum > expected and left < right:
        current_sum -= A_extended[left]
        left += 1

    if current_sum == expected and right - left < N:
        print("Yes")
        exit()

print("No")
