# 1
dog = {}

# 2
dog["name"] = "Snoopy"
dog["colour"] = "Black and White Spotted"
dog["breed"] = "Beagle"
dog["legs"] = 4
dog["age"] = 76

# 3
student = {
    "first_name": "Sofia",
    "last_name": "Muruve",
    "age": 20,
    "gender": "Female",
    "is_married": False,
    "skills": ["French", "Customer Service", "Python"],
    "address": {
        "street": "Fake Road",
        "postal_code": "N0TKN0WN"
        },
    "city": "Toronto",
    "country": "Canada"
}

# 4
print(len(student))

# 5
student["skills"]
print(type("skills")) # is a string, because this checks the type of the key "skills". 
print(type(student["skills"])) # better, because the value of "skills" is the list.

# 6
student["skills"].append("Teamwork") # use append to add one thing to the list existing in student["skills"]
student["skills"].extend(["Communication", "Attention to Detail"]) # or extend for multiple
student["skills"] # check

# 7 - 8
student_keys = student.keys()
print(student_keys)

student_values = student.values()
print(student_values)

# 9
print(student.items())

# 10
type(student["address"])
del student["address"]

# 11
del student