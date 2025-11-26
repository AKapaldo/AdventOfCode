import re

with open('D5.txt', "r") as f:
    input = f.readlines()

def vert():
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for l in input:
        x1 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(1))
        y1 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(2))
        x2 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(3))
        y2 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(4))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x][y1] += 1
    count = 0
    for x in range(1000):
        for y in range(1000):
            if grid[x][y] > 1:
                count += 1
    print(count)
        
    
def diag():
    grid = [[0 for x in range(1000)] for y in range(1000)]
    for l in input:
        x1 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(1))
        y1 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(2))
        x2 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(3))
        y2 = int(re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).group(4))
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][y] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[x][y1] += 1
        else:
            slope = (y2 - y1) / (x2 - x1)
            if slope == 1 or slope == -1:
                if x1 < x2 and y1 < y2:
                    x, y = x1, y1
                    while x <= x2 and y <= y2:
                        grid[x][y] += 1
                        x += 1
                        y += 1
                elif x1 > x2 and y1 < y2:
                    x, y = x1, y1
                    while x >= x2 and y <= y2:
                        grid[x][y] += 1
                        x -= 1
                        y += 1
                elif x1 < x2 and y1 > y2:
                    x, y = x1, y1
                    while x <= x2 and y >= y2:
                        grid[x][y] += 1
                        x += 1
                        y -= 1
                elif x1 > x2 and y1 > y2:
                    x, y = x1, y1
                    while x >= x2 and y >= y2:
                        grid[x][y] += 1
                        x -= 1
                        y -= 1
    count = 0
    for x in range(1000):
        for y in range(1000):
            if grid[x][y] > 1:
                count += 1
    print(count)

vert()
diag()
