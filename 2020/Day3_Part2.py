src='''Source Data Here'''
forest = []
forest = src.splitlines()
def treeLocator(space, line):
    hits = 0
    over = 0
    j = 0
    for i in forest:
        if line == 1:
            if over > 30:
                over = over - 31
            if i[over] == "#":
                hits = hits + 1
                over = over + space
            else:
                over = over + space
        if line == 2:
            j += 1
            if j % 2:
                if over > 30:
                    over = over - 31
                if i[over] == "#":
                    hits = hits + 1
                    over = over + space
                else:
                    over = over + space
    print(hits)


treeLocator(1, 1)
treeLocator(3, 1)
treeLocator(5, 1)
treeLocator(7, 1)
treeLocator(1, 2)
