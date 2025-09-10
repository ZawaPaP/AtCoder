N, M = map(int, input().split())

cities = []

for i in range(1, M + 1):
    p, y = map(int, input().split())
    cities.append((p, y, i))

cities.sort()

result = [''] * M

pref_count = {}

for p, y, original_index in cities:
    if p not in pref_count:
        pref_count[p] = 0
    pref_count[p] += 1
    result[original_index - 1] = f"{p:06d}{pref_count[p]:06d}"

for r in result:
    print(r)
