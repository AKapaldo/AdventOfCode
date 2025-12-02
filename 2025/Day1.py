numbers = list(range(0, 99))
start = 50
password = 0

with open(r"d1.txt", "r") as f:
    input = f.readlines()

def add_combo(a, b, max=100):
    return (a + b) % max

def subtract_combo(a, b, max=100):
    return (a - b) % max

for num in input:
    if num[0] == "L":
        num = int(num[1:])
        start = subtract_combo(start, num)
        if start == 0:
            password += 1
    elif num[0] == "R":
        num = int(num[1:])
        start = add_combo(start, num)
        if start == 0:
            password += 1

print(f'The number of 0s in the combo is: {password}')
