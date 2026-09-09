# Level 1 Exercises
# 1
age = float(input("Enter your age: "))
yearsleft = 18 - age

if age >= 18:
    print("You are old enough to drive")
else:
    print(f"You need {yearsleft} more years to learn to drive.")

# 2 
my_age = 20
your_age = float(input("Enter your age: "))

if your_age > (my_age):
    difference = (your_age - my_age)
    if difference == 1: 
        print("You are 1 year older than me")
    else: 
        print(f"You are {difference} years older than me")

elif your_age < (my_age): 
    difference = (my_age - your_age)
    if difference == 1: 
        print("You are 1 year younger than me")
    else: 
        print(f"You are {difference} years younger than me")

else: 
    print("We are the same age")

# 3
number_one = float(input("Enter number one: "))
number_two = float(input("Enter number two: "))

if number_one > number_two: 
    print(f"{number_one} is greater than {number_two}")
elif number_two > number_one: 
    print(f"{number_two} is greater than {number_one}")
else: 
    print("The two numbers are equal to each other")

# Level 2 Exercises
# 1
grade = float(input("Enter your grade: "))

if 90 <= grade <= 100:
    print("You got an A!")
elif 80 <= grade <= 89:
    print("You got a B!")
elif 70 <= grade <= 79:
    print("You got a C.")
elif 60 <= grade <= 69:
    print("You got a D.")
elif 0 <= grade <= 59:
    print("You got an F.")
else: 
    print("That grade does not exist.")

# 2
month = input("Enter a month to find out what season it's in: ").lower()

autumn = ["september", "october", "november"]
winter = ["december", "january", "february"]
spring = ["march", "april", "may"]
summer = ["june", "july", "august"]

if month in autumn: 
    print("The season is autumn.")
elif month in winter:
    print("The season is winter.")
elif month in spring: 
    print("The season is spring.")
elif month in summer: 
    print("The season is summer.")
else: 
    print("That's not a month!")

# 3
fruits = ["banana", "orange", "mango", "lemon"]
newfruit = input("Name a fruit - is it in my list?").lower()

if newfruit in fruits: 
    print(f"{newfruit} already exists in the list!")
else: 
    fruits.append(newfruit)
    print(f"Now {newfruit} is in the list!")
    print(fruits)

# Level 3 Exercises
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if "skills" in person: 
    num_skills = len(person["skills"])
    print(person["skills"][num_skills // 2]) # printing the middle skill
else: 
    print("This dictionary doesn't include skills!")

if "skills" in person and "Python" in person["skills"]: 
    print(True)

# what kind of developer are they?
FE_Dev = False
BE_Dev = False
FS_Dev = False

if "skills" in person and set(person["skills"]) == {"JavaScript", "React"}: # wanted to control for order, say dictionary puts react before javascript
    print("They are a frontend developer.")
    FE_Dev = True

if "Python" in person["skills"] and "MongoDB" in person["skills"] and "Node" in person["skills"]:
    print("They are a backend developer.")
    BE_Dev = True

if "React" in person["skills"] and "MongoDB" in person["skills"] and "Node" in person["skills"]:
    print("They are a fullstack developer.")
    FS_Dev = True
    
if FE_Dev == BE_Dev == FS_Dev == False:
    print("Unknown Title.")

# and lastly
if person["is_married"] == True and "Finland" in person["country"]: 
    print(f"{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married")