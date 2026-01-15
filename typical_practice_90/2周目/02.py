N = int(input())

if N % 2 == 1:
    exit(0)

temp = []


def recursion(word, open_count, close_count, next, l):
    word += next
    if l == N:
        temp.append(word)
        return

    if open_count == N // 2:
        recursion(word, open_count, close_count + 1, ")", l + 1)
    elif open_count == close_count:
        recursion(word, open_count + 1, close_count, "(", l + 1)
    else:
        recursion(word, open_count + 1, close_count, "(", l + 1)
        recursion(word, open_count, close_count + 1, ")", l + 1)


recursion("", 1, 0, "(", 1)
for w in sorted(temp):
    print(w)
