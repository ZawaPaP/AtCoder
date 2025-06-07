N = int(input())

restaurants = {}

for i in range(1, N + 1):
    s, p = input().split()

    if s in restaurants:
        restaurants[s].append((int(p), i))
    else:
        restaurants[s] = [(int(p), i)]

sorted_restaurants = sorted(restaurants.items(), key=lambda x: x)

for city in sorted_restaurants:
    restaurants = city[1]
    restaurants.sort(reverse=True)

    for restaurant in restaurants:
        print(restaurant[1])
