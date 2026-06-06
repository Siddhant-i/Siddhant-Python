
# It will get the values using  keys

student = {
    "name" : "siddhant",
    "age" : 20,
    "course" : "B.TECH",
    "subject marks" : {
        "phy" : 100,
        "chem" : 20,
        "bio" : 30,
        "maths" : {
            "maths1" : 100,
            "maths2" : 20
        }
    }
}

# print(student.get())  Error

print(student.get("subject marks"))

print(student.get("name"))

print(student.get("name2"))   # none