# It will print all the keys 

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


print(student.keys())

print(student["subject marks"].keys())              # It is a key

# print(student["maths"].keys())                 It is a value of subject maarks