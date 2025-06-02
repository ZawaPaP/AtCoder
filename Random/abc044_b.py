w = input()

words = {}

for char in w:
    if char in words:
        words[char] += 1
    else:
        words[char] = 1

for word_count in words.values():
    if word_count % 2 == 1:
        print("No")
        exit()

print("Yes")
