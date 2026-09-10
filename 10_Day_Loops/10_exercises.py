# Level 1 Exercises
# 1
numbers = list(range(11))

for number in numbers:
    print(number)
number = 0
while number <= 10: 
    print(number)
    number = number + 1

# 2
reverse_numbers = list(range(10, 0, -1))

for number in reverse_numbers:
    print(number)

number = 10
while number >= 0: 
    print(number)
    number = number - 1

# 3
number = 0 # doing a while loop
while number <= 7:
    print("#" * number)
    number = number + 1

for number in range(8): # and a for loop
    if number <= 8:
        print("#" * number)

# 4  
for row in range(8):

    column = 0
    while column < 8:
        print ("# ", end=" ")
        column = column + 1
     

    print()

# 5
for number in range(11): 
    print(f"{number} x {number} = {number ** 2}")

# 6
list = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for word in list: 
    print(word)

# 7
for number in range(101):
    if number % 2 == 0: 
        print(number)

# 8
for number in range(100):
    if number % 2 == 1: 
        print(number)

# Level 2 Exercises
# 1
all_list = []
for number in range(101):
    all_list.append(number)

print(f"The sum of all numbers, from 0 to 100 inclusive, is {sum(all_list)}.")

# 2
even_list = []
for number in range(101):
    if number % 2 == 0:
        even_list.append(number)

odd_list = []
for number in range(100): 
    if number % 2 == 1: 
        odd_list.append(number)

print(f"The sum of all even numbers from 0 to 100 is {sum(even_list)}, and the sum of all odd numbers is {sum(odd_list)}.")

# Level 3 Exercises
# 1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

for country in countries:
    if "land" in country:
        print(country)

# 2
fruits = ["banana", "orange", "mango", "lemon"]
for index in range(len(fruits) -1, -1, -1):
    print(fruits[index])

# 3i
from data.countries_data import countries_data

all_languages = []
for country in countries_data: 
    for language in country["languages"]: 
        all_languages.append(language)

print(all_languages) # noticing duplicates
set_languages = set(all_languages) # make a set
number_languages = len(set_languages) # items in set = number of languages
print(f"there are {number_languages} different languages in countries_data.py")

# 3ii
language_counts = []
for language in set_languages:
    language_counts.append([language, all_languages.count(language)])


most_common = []
while len(most_common) < 10:

    highest = 0

    for pair in language_counts:
        if pair[1] > highest: 
            highest = pair[1]
            highest_pair = pair
            most_common.append(highest_pair)
            language_counts.remove(highest_pair)

print(most_common)