N, K = map(int, input().split())


def eight_to_ten(num):
    eight_num = str(num)
    ten_num = 0
    l = len(eight_num)
    for i in reversed(range(l)):
        ten_num += int(eight_num[i]) * (8 ** (l - 1 - i))

    return ten_num


def base_n(num_10, n):
    str_n = ""
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n

    return int(str_n[::-1])


def replace_eight_to_five(num):
    str_n = str(num)
    new_str = ""
    for i in str_n:
        if i == "8":
            new_str += "5"
        else:
            new_str += i
    return int(new_str)


while K > 0:
    if N == 0:
        break
    base_ten = eight_to_ten(N)
    base_nine = base_n(base_ten, 9)
    N = replace_eight_to_five(base_nine)
    K -= 1

print(int(N))
