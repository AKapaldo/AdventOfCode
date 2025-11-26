src='''Source Here'''
forest = []
forest = src.splitlines()

def treeLocator():
    hits = 0
    over = 0
    for i in forest:
        if over > 30:
            over = over - 31
        if i[over] == "#":
            hits = hits + 1
            over = over + 3
        else:
            over = over + 3
    print(hits)
    
    
treeLocator()
