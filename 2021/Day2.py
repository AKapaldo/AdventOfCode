import re

with open('D2.txt', "r") as f:
    input = f.readlines()

def position():
    hloc = 0
    vloc = 0
    for l in input:
        if re.match('forward (\d+)', l):
            hloc += int(re.match('forward (\d+)', l).group(1))
        elif re.match('down (\d+)', l):
            vloc += int(re.match('down (\d+)', l).group(1))
        elif re.match('up (\d+)', l):
            vloc -= int(re.match('up (\d+)', l).group(1))
    print(f'Location: {hloc * vloc}')

def aim():
    hloc = 0
    vloc = 0
    aim = 0 
    for l in input:
        if re.match('forward (\d+)', l):
            r = re.match('forward (\d+)', l).group(1)
            hloc += int(r)
            vloc += aim * int(r)
        elif re.match('down (\d+)', l):
            aim += int(re.match('down (\d+)', l).group(1))
        elif re.match('up (\d+)', l):
            aim -= int(re.match('up (\d+)', l).group(1))
    print(f'Location: {hloc * vloc}')

position()
aim()
