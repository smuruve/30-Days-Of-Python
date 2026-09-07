# declaring sets first
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1 Exercises
# 1
print(len(it_companies))

# 2 - 4
it_companies.add("Twitter")
it_companies.update(["Nvidia", "Samsung"])
print(it_companies)

it_companies.remove("Facebook") # could use pop for one at random
print(it_companies)

# 5 discard doesn't display errors in attempting to remove a nonexistent item
it_companies.remove("Blackberry")
it_companies.discard("Blackberry")

# Level 2 Exercises
# 1 - 4
A.union(B)
A.intersection(B)
A.issubset(B)
A.isdisjoint(B)

# 5
A.union(B)
B.union(A)

# 6
B.symmetric_difference(A)
A.symmetric_difference(B) #equivalently

# 7
del A
del B

# Level 3 Exercises
# 1
print(f"In list form, ages is {len(age)} items long.")
age_set = set(age)
print(f"In set form, ages is {len(age_set)} items long.")

print(age)
print(age_set) # because sets remove duplicates

# 2 
# Strings are text, and you can't change the characters inside.
# Lists use square brackets and can be modified.
# Tuples use round brackets, can't be changed after they're made. duplicates allowed
# Sets use curly brackets, do not hold duplicate items, are useful for mathematical operations. 
# as per google, you can add/remove elements of a set but not inherently change them.

# 3
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
print(words) # check
words_set = set(words) # now the duplicate words are gone

print(words_set) #out of curiosity
print(len(words_set)) # this is exactly how many unique words (10)