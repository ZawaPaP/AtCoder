N = input()


ans = 0

carry_in = False
for i in reversed(range(len(N))):
    num = int(N[i])
    # 桁借りしていたら - 1
    if carry_in:
        num -= 1

    # 最後の桁
    if i == 0:
        ans += num
        break

    # 最後以外の桁
    else:
        if num == 9:
            ans += 9
            carry_in = False
        else:
            ans += 9
            carry_in = True


print(ans)
