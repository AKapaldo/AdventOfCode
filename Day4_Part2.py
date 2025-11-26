import re
import sys


keys = {
    "byr": r"byr:\s*(19[2-9]\d|200[0-2])\b",
    "iyr": r"iyr:\s*20(1\d|20)\b",
    "eyr": r"eyr:\s*20(2\d|30)\b",
    "hgt": r"hgt:\s*(1([5-8]\d|9[0-3])cm|(59|6\d|7[0-6])in)",
    "hcl": r"hcl:\s*#[0-9a-f]{6}\b",
    "ecl": r"ecl:\s*(amb|blu|brn|gry|grn|hzl|oth)\b",
    "pid": r"pid:\s*\d{9}\b",  
}

with open(sys.argv[1], "r") as f:
    passports = f.read().split("\n\n")

num_data_valid = sum([all([re.search(keys[k], p) for k in keys]) for p in passports])
print(f"Valid: {num_data_valid}")
