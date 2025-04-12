N = int(input())

isLoggedin = False

error_count = 0

for _ in range(N):
    S = input()

    match S:
        case "login":
            isLoggedin = True
        case "logout":
            isLoggedin = False
        case "private":
            if isLoggedin:
                continue
            else:
                error_count += 1
        case "public":
            continue
        case _:
            exit()

print(error_count)
