# Import Functions
import re

# Import Data
data = '''
<Data here>
'''

# Perform Regex; Left: get first digit, right: ignore first digit and spaces then grab second digit
left_pattern = r'^\d{5}'
right_pattern = r'(?!^.{8})(\d{5})'
left = re.findall(left_pattern, data, flags=re.MULTILINE)
right = re.findall(right_pattern, data, flags=re.MULTILINE)

# Convert Strings to Int
l_num = [int(i) for i in left]
r_num = [int(i) for i in right]

# Sort list small to large
l_num.sort()
r_num.sort()


# Count number of times each left number shows in right list and multiply them together, then add the sum of all products
total = sum(x * r_num.count(x) for x in l_num)


# Print out the answer
print(total)
