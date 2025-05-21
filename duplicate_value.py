# PROBLEM: Check for duplicate values in list

# SOLUTION
x = [1,2,3,4,2,5,3,2]

if len(set(x)) == len(x):
    print(False)
else:
    print(True)

# A set cannot have duplicate items. The set() constructor creates a set object from the list (x).
# If the lenght the set equals the lenght of the list, then there are no duplicate. But, if the length of the 
# set is not the same as the lenght of the list, there are one or more duplicate values.


