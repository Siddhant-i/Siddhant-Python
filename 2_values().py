# It will print all the values 

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

print(student.values())

# print(student["name"].values())          It is key

studentvalues = student.values()
print(studentvalues)