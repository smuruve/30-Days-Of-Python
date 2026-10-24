# Level 2
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
import functools

# 1
countries_upper = list(map(str.capitalize, countries)) # use list to convert generic map object
print(countries_upper)

# 2
numbers_squared = list(map(lambda number: number ** 2, numbers))
print(numbers_squared)

# 3
names_upper = list(map(lambda name: name.upper(), names)) # lambda applies upper to a str in names
print(names_upper) # map iterates through each name in names

# 4
def contains_land(country: str) -> bool: 
    return "land" not in country

countries_not_land = filter(contains_land, countries)
print(list(countries_not_land))

# try a lambda function for 4
lambda_countries_not_land = filter(lambda country: "land" not in country, countries)
print(list(lambda_countries_not_land))

# 5
def is_six(country: str) -> bool:
    return len(country) != 6

countries_not6 = filter(is_six, countries)
print(list(countries_not6))

# trying a lambda expression
lambda_countries_not6 = filter(lambda country: len(country) != 6, countries)
print(list(lambda_countries_not6))

# 6
countries_under6 = filter(lambda country: len(country) < 6, countries)
print(list(countries_under6)) # empty list, as length of countries all at least 6

# 7
not_start_e = filter(lambda country: country[0] != "E", countries)
print(list(not_start_e)) # removes estonia

# 8
# multiply each number in numbers by 2 (map), keep those under 9 (filter) 
doubled_and_sub9 = list(
    filter(lambda number: number < 9, # keep numbers under 9
           map(lambda number: number * 2, numbers
               ) # among doubled numbers
        )
)
print(doubled_and_sub9)

# 9
def get_string_lists(my_list: list) -> list[str]:
    str_list = list(filter(lambda item: isinstance(item, str), my_list))
    return str_list

# 10
import functools
from functools import reduce

def add_two_nums(x: int, y: int) -> int:
    return x + y

summed_numbers = reduce(add_two_nums, numbers)
print(summed_numbers)

# 11
def concatenate(str1: str, str2: str) -> str:
    return str1 + ", " + str2

country_string = reduce(concatenate, countries[:-1]) # leave out iceland
country_sentence = f"{country_string} and {countries[-1]} are north European countries"
print(country_sentence)

# 12
# characteristic of choice: remove if contains lowercase or uppercase "s"
from countries import countries

def no_s_allowed(country: str) -> bool:
    return "s" not in country.lower()

def categorize_countries(country_list: list) -> list:
    sans_s = filter(no_s_allowed, country_list)
    return list(sans_s)

print(categorize_countries(countries))

# 13
def create_country_dict(countrylist: list):
    country_dict = {}

    for country in countrylist: 
        letter = country[0]

        if letter in country_dict:
            country_dict[letter] += 1
        else: 
            country_dict[letter] = 1

    return country_dict

print(create_country_dict(countries))

# 14
def get_first_ten_countries(countrylist: list):
    return countries[:10]

print(get_first_ten_countries(countries))

# 15
def get_last_ten_countries(countrylist: list):
    return countries[-10:]

print(get_last_ten_countries(countries))

    
    

    
