import re

def split(word):
    return [char for char in word]

src = '''Source Input Here'''
pos1 = '(\d+)-'
pos2 = '\d+-(\d+)'
char = '\d+-\d+ (\w)'
pw = '\d+-\d+ \w: (\w+)'

repos1 = []
repos2 = []
rechar = []
repw = []
pwchars = []
valid = 0

repos1 = re.findall(pos1, src)
repos2 = re.findall(pos2, src)
rechar = re.findall(char, src)
repw = re.findall(pw, src)


for i in range(len(repw)):
    pwchars = split(repw[i])
    j = int(repos1[i]) - 1
    k = int(repos2[i]) - 1
    if pwchars[j] == rechar[i]:
        pwpos1 = True
    else:
        pwpos1 = False
    if pwchars[k] == rechar[i]:
        pwpos2 = True
    else:
        pwpos2 = False
    if pwpos1 == True and pwpos2 == False:
        valid += 1
    elif pwpos1 == False and pwpos2 == True:
        valid += 1

print(valid)
