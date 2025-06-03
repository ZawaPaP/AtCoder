N = int(input())

W = []
words = set()
last_char = ""
ans = True

for _ in range(N):
    word = input()
    W.append(word)

for word in W:
    if word in words:
        ans = False

    words.add(word)

    if last_char and last_char != word[0]:
        ans = False
    else:
        last_char = word[-1]

if ans:
    print("Yes")
else:
    print("No")
