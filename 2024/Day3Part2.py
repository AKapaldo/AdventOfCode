# Import Functions
import re

# Import Data
data = ''' 
<data here>
'''

# fix data to always have a do at the start and don't at end
data = "do()" + data + "don't()"

# Define Variable
answer = 0 

# Define Regex
pattern = r'mul\(\d+,\d+\)'
do = r'do\(\)'
do_not = r'don\'t\(\)'
do_pattern = f"{do}(.*?){do_not}"


# Get data between do and don't
captured_data = re.findall(do_pattern, data, re.DOTALL)

# Capture mul sequences
for x in captured_data:
    mul = re.findall(pattern, x)

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
