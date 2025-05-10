# PROBLEM: Check for duplicate values in list

# SOLUTION
x = [1,2,3,4,2,5,3,2]

if len(set(x)) == len(x):
    print(False)
else:
    print(True)


