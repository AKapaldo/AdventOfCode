import sys

with open(sys.argv[1], "r") as f:
    tickets = f.read().split("\n")

all_seats = [int(
    (l.replace('B','1').replace('F','0')
    .replace('R','1').replace('L','0'))
    ,2) for l in tickets]


print(f"Max value: {max(all_seats)}")
print(f"Seat: {sum(range(sorted(all_seats)[0],sorted(all_seats)[-1]+1)) - sum(sorted(all_seats))}")
