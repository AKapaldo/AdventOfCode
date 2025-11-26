with open('D1.txt', "r") as f:
    input = f.readlines()

def increase():
    total = 0
    p = 9999

    for n in input:
        if int(n) > p:
            total += 1
        p = int(n)

    print(total)


def compare():
    total = 0
    p = 9999
    for n in range(len(input)):
        try:
            if int((input[n])) + int((input[n+1])) + int((input[n+2])) > p:
                total += 1
        except IndexError:
            break
        try:
            p = int((input[n])) + int((input[n+1])) + int((input[n+2]))
        except IndexError:
            break
    print(total)


increase()
compare()
