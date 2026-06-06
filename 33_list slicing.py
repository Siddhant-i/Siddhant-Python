
# list_name[ Starting_index : Ending_index]      #Ending_index not included

marks = [10,20,30,40,50,"Siddhant","Nandini","Sammu","Bada","Tammana"]

print(marks[2:8])

print(marks[ : 6])

print(marks[7 :])        # len(str) = last index 
                         # len(marks)

# positive slicing indexing : (left to right)  // 0 1 2 3 4 5 ......len(str)

# negative slicing indexing (right to left)    //  -5 -4 -3 -2 -1 

print(marks[-3:-1])                             # -1 = Ending index (not included)

print(marks[-7:-3])