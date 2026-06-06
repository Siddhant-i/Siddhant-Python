
# Update  - it is used to Add new values or CXhange new values


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
            "maths2" : 20,
        }
    }
}

print(student.update({"city":"Bhopal"}))          # value print none

print(student.update({"age":40}))                 # value print none
 
print(student)               # updated value