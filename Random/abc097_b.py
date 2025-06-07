X = int(input())


# 1は何乗しても1のため、先に入れておく
beki_jo = [1]

for i in range(2, X):
    for j in range(2, X):
        if i**j > X:
            break

        beki_jo.append(i**j)

print(max(beki_jo))
