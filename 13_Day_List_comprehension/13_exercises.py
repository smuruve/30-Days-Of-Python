# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
sub_zero = [x for x in numbers if x <= 0]
print(sub_zero)

# 2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
unified_list = [item for sublist in list_of_lists for item in sublist]
print(unified_list)

# for my understanding, this is equivalent to 
unified_list2 = []

for sublist in list_of_lists: 
    for item in sublist: 
        unified_list2.append(item)

print(unified_list2)

# 3
tuple_list = [(n, n ** 0, n ** 1, n ** 2, n ** 3, n ** 4, n ** 5) for n in range(11)]
print(tuple_list)

# 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_caps = [
    [country.upper(), country[:3].upper(), capital.upper()]
    for sublist in countries
    for country, capital in sublist
]

print(country_caps)

# 5
country_dict = [
    {"country": country.upper(), "city": city.upper()} 
    for sublist in countries
    for country, city in sublist
]

print(country_dict)

# 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
combined_names = [
    firstname + " " + lastname # what I want to do
    for name in names # to each inner list in names
    for firstname, lastname in name # for each tuple in the inner list
    ]

print(combined_names)

# 7
slope = lambda x1, y1, x2, y2: (y2 - y1)/(x2 - x1)

print(slope(6, 2, 8, 1)) # - 0.5
