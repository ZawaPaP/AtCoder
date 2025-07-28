N = int(input())
H = list(map(int, input().split()))

count = 0
watering = False

while True:
    watering = False
    for i in range(N):
        if H[i] == 0:
            watering = False
            continue

        if not watering:
            count += 1
            watering = True
        H[i] -= 1

    if sum(H) == 0:
        break

print(count)
