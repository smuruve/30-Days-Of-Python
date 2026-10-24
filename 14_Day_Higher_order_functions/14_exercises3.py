# Level 3
from countries_data import countries_data

# sort by name
countries_by_name = []
sort_by_name = sorted(countries_data, key=lambda country: country["name"])

for country in sort_by_name:
    countries_by_name.append(country["name"])
    
print(countries_by_name)

# sort by capital
countries_by_capital = []
sort_by_capital = sorted(countries_data, key=lambda country: country["capital"])

for country in sort_by_capital:
    countries_by_capital.append(country["capital"])
    
print(countries_by_capital)

# sort by population
countries_by_pop = []
sort_by_pop = sorted(countries_data, key=lambda country: country["population"])

for country in sort_by_pop:
    countries_by_pop.append(country["population"])
    
print(countries_by_pop)

# ten most spoken languages by location
language_counts = {} # hold language and count pairs

for country in countries_data: 
    for language in country["languages"]: 
        if language not in language_counts:
            language_counts[language] = 1
        else:
            language_counts[language] += 1


sorted_languages = sorted(
    language_counts.items(), # iterable
    key=lambda item: item[1], # sort by the count (value) not language name (key)
    reverse = True 
)

top10_languages = sorted_languages[:10]
print(top10_languages)


# 10 most populated countries: borrow from above
top10_pop = []
country_pop = []
sort_by_pop_descending = sorted(countries_data, key=lambda country: country["population"], reverse = True)

for country in sort_by_pop_descending[:10]:
    country_pop.extend([country["name"], country["population"]])
    top10_pop.append(country_pop)
    country_pop = []

print(top10_pop)
