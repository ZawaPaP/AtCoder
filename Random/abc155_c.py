N = int(input())

dict = {}

for _ in range(N):
    word = input()
    dict[word] = dict.get(word, 0) + 1

dict_sorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)

ans_words = []

max_count = dict_sorted[0][1]

for item in dict_sorted:
    if item[1] < max_count:
        break

    ans_words.append(item[0])

ans_words.sort()

for a in ans_words:
    print(a)
