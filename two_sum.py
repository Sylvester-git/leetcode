# PROBLEM: Given an array of integers nums and an integer target, return the indecies of the twoo numbers such that they add up to the target

# SOLUTION

x = [7,11,2,5,10]

target = 15

# Map to store the values of x and their index
hash_map = {}

for i in x:
    # Check for if the value of the value of i subtractd from the target exist in the map
    if target - i in hash_map:
        print(f"Indecies are {hash_map[target - i]} and {x.index(i)}")
    else:
        # Add the value and its index if it doesn't exist
        hash_map[i] = x.index(i)
    