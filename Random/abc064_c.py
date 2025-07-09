N = int(input())
A = list(map(int, input().split()))

scores = {
    "Gray": 0,
    "Brown": 0,
    "Green": 0,
    "Water": 0,
    "Blue": 0,
    "Yellow": 0,
    "Purple": 0,
    "Red": 0,
}

overs = 0
for a in A:
    if a < 400:
        scores["Gray"] += 1
    elif a < 800:
        scores["Brown"] += 1
    elif a < 1200:
        scores["Green"] += 1
    elif a < 1600:
        scores["Water"] += 1
    elif a < 2000:
        scores["Blue"] += 1
    elif a < 2400:
        scores["Yellow"] += 1
    elif a < 2800:
        scores["Purple"] += 1
    elif a < 3200:
        scores["Red"] += 1
    else:
        overs += 1

count = 0
for v in scores.values():
    if v > 0:
        count += 1


print(max(1, count), count + overs)
