N, K = map(int, input().split())

A = list(map(int, input().split()))

MOD = 10 ** 9 + 7

tento_count = 0

for i in range(N):
	for j in range(i + 1, N):
		if A[i] > A[j]:
			tento_count += 1

second_tento_count = 0

for i in range(N):
	for j in range(N):
		if A[i] > A[j]:
			second_tento_count += 1

total = tento_count * K + second_tento_count * K * (K - 1) // 2

print(total % MOD)