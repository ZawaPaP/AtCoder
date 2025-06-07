N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

temperatures = []

for h in H:
    temperatures.append(T - h * 0.006)


ans = -1
temp_diff = float("inf")
for i, temperature in enumerate(temperatures):
    if abs(A - temperature) < temp_diff:
        temp_diff = abs(A - temperature)
        ans = i

print(ans + 1)
