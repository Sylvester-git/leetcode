# PROBLEM: Check the given list for missing numbers range (1,len(nums))

# SOLUTION

x = [4,4,5,7,1,2,2]

missing_number = []

set_num = set(x)

# In this case it will be 1 => 10
for i in range(1, len(x)+1):
    if i not in set_num:
        missing_number.append(i)

print(missing_number)