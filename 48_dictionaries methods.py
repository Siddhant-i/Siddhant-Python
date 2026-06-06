
student = {
    "name" : "Siddhant Raghuvanshi",
    "age" : 19,
    "subjects marks" : {
        "maths" : {
            "Maths1" : 100,
            "Maths2" : 90
        },
        "Science" : {
            "phy" : 100,
             "chem" : 100,
              "bio" : 100,
        }
    }
}




# dictionary_name.keys()

print(student.keys())
print(student["subjects marks"].keys())


# dictionary_name.values()

print(student.values())
print(student["subjects marks"].values())

# dictionary_name.items()

print(student.items())


# dictionary_name.get("key")

print(student.get("name"))
print(student.get("subjects marks"))           

print(student.get("science"))                                     # Value

# dictionary_name.update(new dictionary)


studentupdate = student.update({"city":"Bhopal"})
print(student.update({"city" : "Bhopal"}))