S = input()

directions = {"N": 0, "S": 0, "E": 0, "W": 0}

for s in S:
    if s in directions:
        directions[s] += 1


if (directions["N"] > 0 and directions["S"] > 0) or directions["N"] == directions["S"]:
    if (directions["W"] > 0 and directions["E"] > 0) or directions["W"] == directions[
        "E"
    ]:
        print("Yes")
        exit()
print("No")
