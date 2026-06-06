# Waap to cheak if a list contains a palindrome of elememts

# palindrome = starting order == reverse order 

# [1,2,3,2,1]

# ('a','i','o','i','a')


list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("Not palindrome")