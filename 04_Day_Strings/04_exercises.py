# first attempt concatenation
word1 = "Thirty "
word2 = "Days "
word3 = "Of "
word4 = "Python "

first_string = word1 + word2 + word3 + word4
print(first_string)

# 2 second attempt concatenation
word5 = "Coding "
word6 = "For "
word7 = "All"
second_string = word5 + word6 + word7
print(second_string)

# 3 - 7
company = second_string
print(company)
print(len(company))
print(company.upper())
print(company.lower())

# 8
print(second_string.capitalize())
print(second_string.title())
print(second_string.swapcase())

# 9 
print(second_string[7:]) #including only the first 7
print(second_string[-8:]) #alternatively, the last 8 characters

# 10 will use both index and find
print(second_string.index("Coding"))
print(second_string.find("Coding"))
print("Coding" in second_string) # for fun

# 11
print(second_string.replace("Coding", "Python"))

# 12 
replacedcoding = (second_string.replace("Coding", "Python")) #saving #11 work to a variable
replacedpython = (replacedcoding.replace("All", "Everyone")) #replacing second difference
print(replacedpython)   
# now "Python For Everyone" exists as a string.
print(replacedpython.replace("Everyone", "All"))  #change back to "Python for All"

# 13
print(second_string.split("A"))

# 14
third_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(third_string.split(", ")) # adding the space after the comma in the separator means both comma and space get removed

# 15 - 17
print(second_string[0])
print(second_string[-1])
print(second_string[10]) # a space!

# 18
print(replacedpython[0], replacedpython[7], replacedpython[11])

# 19
print(second_string[0], second_string[7], second_string[11])

# 20 - 21
print(second_string.index("C"))
print(second_string.index("F"))

#22
fourth_string = "Coding For All People"
print(fourth_string.rfind("l"))
print(len(fourth_string)) 

# 23 - 27
sentence = "You cannot end a sentence with because because because is a conjunction"
print(sentence.index("because")) #first occurrence
print(sentence.rindex("because")) # last occurrence
print(sentence.find("because"))
print(sentence.rfind("because")) #index and find interchangeable here

print(sentence.replace("because because because ", "")) #my first way
print(sentence[:30] + sentence[54:])

# 28 - 29
print(second_string.startswith("Coding"))
print(second_string.endswith("coding"))

# 30
space_string = "   Coding For All      "
print(space_string.index("C"))
print(space_string.rindex("l"))
print(space_string[3:17]) #start at 3 where you want to see the C, end at 17 where you want python to stop including.
#shorter language: slicing is start inclusive, stop-exclusive

# 31
testvar1 = "30DaysofPython"
testvar2 = "thirty_days_of_python"
print(testvar1.isidentifier())
print(testvar2.isidentifier())

# 32
librarylist = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
"# ".join(librarylist)

#33
print("\nI am enjoying this challenge. \nI just wonder what \nis next.")

#34
print("Name\tAge\tCountry\tCity")
print("Sofia\t20\tCanada\tToronto")

#35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} metres square")

#36
number1 = 8
number2 = 6
# using f-strings
print(f"{number1} + {number2} = {number1 + number2}")
print(f"{number1} - {number2} = {number1 - number2}")
# using str.format
print("{} * {} = {}".format(number1, number2, number1 * number2))
print("{} / {} = {}".format(number1, number2, number1 / number2))
# using old style %
print("%d %% %d = %d" %(number1, number2, number1 % number2))
print("%d // %d = %d" %(number1, number2, number1 // number2))
print("%d ** %d = %d" %(number1, number2, number1 ** number2))