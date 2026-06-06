# Wap to count the number of students with "A" grade in  user input and store the values in a list and sort them from  "A" to "D"


print("Enter grades : 'A','B','A+','C','D'")



grade1 = input("Enter yours grade  : ")
grade2 = input("Enter yours grade  : ")
grade3 = input("Enter yours grade  : ")
grade4 = input("Enter yours grade  : ")
grade5 = input("Enter yours grade  : ")
grade6 = input("Enter yours grade  : ")
grade7 = input("Enter yours grade  : ")

grades = [grade1,grade2,grade3,grade4,grade5,grade6,grade7]

print("Students grade are : ",grades)


print("The students with grade 'A' are : ",grades.count("A"))


# Sorting from A to D

grades.sort()
print("The sorted grades are : ",grades)

grades.sort(reverse = False)
print("The sorted grades are : ",grades)

grades.sort(reverse = True)
print("The sorted grades in decending order are : ",grades)
