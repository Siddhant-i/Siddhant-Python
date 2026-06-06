
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

student.pop("course")           # element pop

print(student.pop("age"))        # pop value print

student.pop("subject marks")

print(student)