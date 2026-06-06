# Wap to count the number of srudents with "A" grade in the following tuple with a user input

print("Enter grades : 'A','B','A+','C','D'")

grade1 = input("Enter yours grade  : ")
grade2 = input("Enter yours grade  : ")
grade3 = input("Enter yours grade  : ")
grade4 = input("Enter yours grade  : ")
grade5 = input("Enter yours grade  : ")
grade6 = input("Enter yours grade  : ")
grade7 = input("Enter yours grade  : ")

grades = (grade1,grade2,grade3,grade4,grade5,grade6,grade7)

print("Students grade are : ",grades)


print("The students with grade 'A' are : ",grades.count("A"))
