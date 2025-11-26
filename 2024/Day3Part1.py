# Import Functions
import re

# Import Data
data = ''' 
<Data Here>
'''

# Define Variable
answer = 0 

# Define Regex
pattern = r'mul\(\d+,\d+\)'

# Capture mul sequences
mul = re.findall(pattern, data)

# do math
for i in mul:
    # Capture just the numbers
    num_pattern = r'(?!mul\()(\d+)'
    nums = re.findall(num_pattern, i)

    # Convert the numbers from str to int
    int_num = [int(i) for i in nums]

    # Multiply numbers
    product = int_num[0] * int_num[1]

    answer += product

print(answer)

