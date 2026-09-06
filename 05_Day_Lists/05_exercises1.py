# Level 1 Exercises
# 1
emptylist = list()

# 2 - 4
peakveg = ["carrots", "spinach", "tomatoes", "fennel", "mushrooms", "beets"]
len(peakveg)
print("the first item of my list is", peakveg[0], "the last item is", peakveg[-1], "and I believe the middle item is either", peakveg[3], "or", peakveg[4], "because my list is 6 items long.")

# 5
mixed_data_types = ["Sofia", 20, "unmarried", "you are not getting my address", 11.1]
print(mixed_data_types)

# 6 - 9
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(f"The first company is {it_companies[0]}, the middle company is {it_companies[len(it_companies) // 2]}, and the final company is {it_companies[-1]}.")

# 10
it_companies.pop(1)
it_companies.append("Google2")
print(it_companies)

# 11 - 15
it_companies.append("Nvidia")

print(len(it_companies) // 2) # finding the middle
it_companies.insert(4, "Samsung")
print(it_companies)

it_companies.pop(-2)
it_companies.insert(-2, "GOOGLE")
print(it_companies)

"#; ".join(it_companies)

"GOOGLE" in it_companies

# 16 - 17
it_companies.sort()
print(it_companies) # check

it_companies.reverse()
print(it_companies) # check

# 18 - 20
slice18 = it_companies[3:]
print(slice18)

slice19 = it_companies[:-3]
print(slice19)

slice20 = it_companies[:len(it_companies) // 2] + it_companies[(len(it_companies) // 2) + 1 :] 
print(slice20)

#21 - 25
it_companies.pop(0) # using pop only needing to do one index
it_companies.pop(len(it_companies) // 2)
it_companies.pop(-1) # could have done pop() too
it_companies.clear()
print(it_companies) # check

# 26
front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
list26 = front_end + back_end
print(list26)

# 27
list27 = list26.copy()
fullstack = list27
print(fullstack) # checking once
print(fullstack == list26 == list27) # checking twice for fun
fullstack.index("Redux") # thus put "Python", "SQL" at indices 5, 6

fullstack.insert(5, "Python")
fullstack.insert(6, "SQL")
print(fullstack)