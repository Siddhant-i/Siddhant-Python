# student = {"name": "Siddhant", "age": 19}

# 1. Print all keys
# 2. Add city = Bhopal
# 3. Remove age
# 4. Print key-value pairs



student = {"name": "Siddhant", "age": 19}


print(student.keys())

student.update({"city":"Bhopal"})
student.pop("age")

print(student)

print(student.items())