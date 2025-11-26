import statistics, math

with open('D7.txt', "r") as f:
    input = list(map(int, f.read().split(",")))

def crab_median():
    median = int(statistics.median(input))
    fuel = []

    for c in range(len(input)):
        fuel.append((abs(median - input[c])))

    return(sum(fuel))

def crab_mean():
    mean = math.floor(statistics.mean(input))
    fuel = []
    for c in range(len(input)):
        n = abs(mean - input[c])
        fuel.append(abs(int(n*(n+1)/2)))
        
    return(sum(fuel))

print(f'Part 1: {crab_median()}')
print(f'Part 2: {crab_mean()}')
