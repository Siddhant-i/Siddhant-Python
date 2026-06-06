# It will print all the items ("keys" : "values")

# it will get all the key : value pairs

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

print(student.items())

studentitem = student.item()
print(studentitem)