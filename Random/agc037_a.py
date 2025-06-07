s = input().strip()

"""文字列を隣り合う部分文字列が異なるように分割する"""
if not s:
    print(0)
    exit()

words = []
current = ""
prev = ""

for char in s:
    current += char
    if current != prev:
        words.append(current)
        prev = current
        current = ""

# 最後の文字列が残っている場合
if current:
    if current == prev:
        print(len(words))
        exit()
    words.append(current)


print(len(words))
