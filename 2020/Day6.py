import sys

with open(sys.argv[1], "r") as f:
    input = f.read().split("\n\n")

def customs_questions(customs):
    for i in range (len(customs)):
        customs[i] = customs[i].replace('\n', '')

    letters = 0

    for l in customs:
        letters += len(set(l))
        
    print(letters)

def diff_customs(customs):
    for i in range (len(customs)):
        customs[i] = customs[i].replace('\n', ' ')
    letters = 0 

    for l in customs:
        group = []
        group += l.split()
        letters += len(set(group[0]).intersection(*group))
    print(letters)


diff_customs(input) #Part 2
customs_questions(input) #Part 1 - Comment out to run 1 at a time
