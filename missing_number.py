# PROBLEM: Check list for one missing number in range [0,n]

# SOLUTION:
x  = [0,1,2,4]

print(f"Lenght of list {len(x)}")

# This the sum of the list if it was complete
# NOTE: One is added to include the last number
print(f"Sum of list when complete: {(sum(range(len(x)+1)))}")

# This is the sum of the actuall list
print(f"Sum of actual list: {sum(x)}")

# Print out the missing value
print(f"Missing value: {(sum(range(len(x)+1)) - sum(x))}")