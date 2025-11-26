import re
src = '''Source Here'''
passports = []
valid = 0
passports = src.split("\n\n")
for i in range (len(passports)):
    passports[i] = passports[i].replace('\n', ' ')

for i in passports:
    byr = re.findall('byr:', i)
    iyr = re.findall('iyr:', i)
    eyr = re.findall('eyr:', i)
    hgt = re.findall('hgt:', i)
    hcl = re.findall('hcl:', i)
    ecl = re.findall('ecl:', i)
    pid = re.findall('pid:', i)
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        valid += 1

print(valid)
