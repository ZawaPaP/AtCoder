N = int(input())

Works = []

for _ in range(N):
    A, B = map(int, input().split())
    Works.append((A, B))

Works.sort(key=lambda x: x[1])

current_time = 0

for work in Works:
    current_time += work[0]
    if current_time > work[1]:
        print("No")
        exit()
print("Yes")
