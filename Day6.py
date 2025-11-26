with open('D6.txt', "r") as f:
    input = list(map(int, f.read().split(",")))

def ocean1(days):
    for _ in range(days):
        for f in range(len(input)):
            if input[f] > 0:
                input[f] -= 1
            elif input[f] < 1:
                input[f] = 6
                input.append(8)
    print(len(input))

def ocean2(fish, days):
    input = [fish.count(i) for i in range(9)] 
    for _ in range(days):
        zero_count = input[0]
        input[:-1] = input[1:] 
        input[6] += zero_count
        input[8] = zero_count 
    print(sum(input))

ocean2(input, 256)
