import re
min1 = '(\d+)-'
max1 = '\d+-(\d+)'
char = '\d+-\d+ (\w)'
pw = '\d+-\d+ \w: (\w+)'
src = '''Source Values Here'''

remax = []
remin = []
rechar = []
repw = []
valid = 0

remin = re.findall(min1, src)
remax = re.findall(max1, src)
rechar = re.findall(char, src)
repw = re.findall(pw, src)

for i in range(len(repw)):
    recount = re.findall(rechar[i], repw[i])
    long = len(recount)
    if int(remin[i]) <= int(long) <= int(remax[i]):
        valid += 1

print(valid)
