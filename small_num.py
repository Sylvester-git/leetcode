# HOW MANY NUMBERS ARE SMALLER THAN THE CURRENT NUMBER

# EXAMPLE 1

"""
INPUT: nums = [8,1,2,2,3]
OUTPUT: [4,0,1,1.3]
EXPLANATION: For nums[0]=8 there exist four smaller numbers than it in the array. (4)
             For nums[1]=1, does not exist any smaller number than it.
             For nums[2]=2 there exist one smaller number than it (1)
"""

# EXAMPLE 2

"""
INPUT: nums = [7,7,7,7,7]
OUTPUT: [0,0,0,0,0]

"""

nums = [8,1,2,2,3]
 
# First step is to sort the list
sorted = sorted(nums)

# A map to hold the number and its index
d = {}

# This will be ued to output the list
ret = []

# This loops through the sorted list.
# If the number and its index does not exist inside the map, it is added.
for i in sorted:
    if i not in d:
        d[i] = sorted.index(i)

# This loops through the unsorted list
# It adds the value of the number from the map to the list
for i in nums:
    ret.append(d[i])

# Prints out the value
print(ret)
