import re  

data = '''
<numbers here>
'''

# Capture digits in rows and conver to int
rows = [[int(n) for n in re.findall(r"\d+", line)] for line in data.splitlines()]



# determine safe or not
def is_safe(row):
    #calculate the differences in each row
    diffs = [row[i+1] - row[i] for i in range(len(row)-1)]

    # If any difference is 0 or >3 or <-3, unsafe
    if any(d == 0 or abs(d) > 3 for d in diffs):
        return False

    # Check direction consistency (all positive or all negative)
    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)

    return all_increasing or all_decreasing

safe = 0
unsafe = 0 

for row in rows:
    if is_safe(row):
        safe += 1
    else:
        unsafe += 1

print(f"Safe: {safe}\nUnsafe: {unsafe}")
