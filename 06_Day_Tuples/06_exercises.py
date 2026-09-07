# Level 1 Exercises
#1
tuple() 

#2
sisters = ("Jasmine",) # apparently you have to add a comma after to make it a tuple
brothers = ("Marc",)  # rather than a regular string

#3
siblings = sisters + brothers
print(siblings) 

#4
print(len(siblings))

#5
sibling_mod = list(siblings)
sibling_mod.append("Lily")
sibling_mod.append("Richard")
print(sibling_mod)
family_members = tuple(sibling_mod)
print(family_members)

# Level 2 Exercises
#1 unpacking means tuple --> variables
a, b, c, d = family_members
siblings = a, b
parents = c, d

print(f"siblings are as follows: {siblings}")
print(f"parents are as follows: {parents}")

# 2
fruits = ("Apple", "Kiwi", "Clementine", "Blueberry", "Lime", "Papaya")
vegetables = ("Carrot", "Cabbage", "Lettuce", "Radish", "Tomato")
animal_products = ("Eggs", "Milk", "Butter", "Cheese", "Ground Beef")

food_stuff_tp = fruits + vegetables + animal_products

# 3
food_stuff_list = list(food_stuff_tp)

# 4 
len(food_stuff_list) # even, at 16
middle = len(food_stuff_list) // 2 #technically right middle, indexing starts at 0
print(food_stuff_list[middle - 1:middle + 1]) # start at left middle [7], include [8], stop before [9]

# 5 
print(food_stuff_list[3:-3])

# 6
del food_stuff_list

# 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
"Estonia" in nordic_countries
"Iceland" in nordic_countries