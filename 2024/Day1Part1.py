# Import Functions
import re

# Import Data
data = '''
# Numbers Here
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

# Subtract numbers and always have positive value with abs
result = [abs(x -y) for x, y in zip(l_num, r_num)]

# Get total distance
total = sum(result)

# Print out the answer
print(total)
