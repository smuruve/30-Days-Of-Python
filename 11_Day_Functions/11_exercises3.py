# Level 3 Exercises
# 1
def is_prime(n: float):
    if n <= 1: 
        return False
    if n == 2: 
        return True
    elif n % 2 == 0:
        return False
    else: 
        for number in range(3, int(n ** 0.5) + 1, 2): # odd factors up to the square root
            if n % number == 0:
                return False
    return True

is_prime(15)

# 2
def duplicates_present(my_list): 
    return len(my_list) > len(set(my_list))
        
fruits = ["kiwi", "mango", "cherry", "mango", "dragonfruit"]
uniquenumbers = [1, 2, 3, 4, 5, 6]

duplicates_present(fruits)
duplicates_present(uniquenumbers)

# 3
def unique_type_list(my_list):
    diff_types = set()
    for item in my_list:
        diff_types.add(type(item))
    print(f"This list has items of {len(diff_types)} different data types")
    return diff_types

uniform_list = [1, 20, 30, 41]
unique_list = ["mango", 24.5, 20, True, "kiwi"]
unique_type_list(uniform_list)
unique_type_list(unique_list) 

# 4
def is_variable_valid(variable_name):
    return variable_name.isidentifier()

# 5
from data.countries_data import countries_data
print(countries_data)

def most_spoken_languages(countries_data):
    language_counts = {}
    for country in countries_data:
        for language in country["languages"]:
            if language not in language_counts: 
                language_counts[language] = 1
            else: 
                language_counts[language] = language_counts[language] + 1

    top20_languages = []
    while len(top20_languages) < 20:
        highest = max(language_counts.values())

        for language in language_counts:
            if language_counts[language] == highest:
                top20_languages.append(language)
                break

        del language_counts[language]

    return(top20_languages)

most_spoken_languages(countries_data)


def most_populated_countries(countries_data):
    populations = {}
    for country in countries_data:
        populations[country["name"]] = country["population"]

    country_names = []
    while len(country_names) < 10: 
        largest = max(populations.values())

        for country in populations: 
            if populations[country] == largest:
                country_names.append(country)
                break
        del populations[country]

    return country_names

most_populated_countries(countries_data)