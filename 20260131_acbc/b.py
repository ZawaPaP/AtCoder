N, K = map(int, input().split())

age = N
sum = age
year = 0

while sum < K:
    year += 1
    age += 1
    sum += age

print(year)
