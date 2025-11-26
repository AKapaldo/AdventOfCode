from collections import Counter

with open('D3.txt', "r") as f:
    input = f.readlines()

def PowerConsumption():
    a, b, c, d, e, g, h, i, j, k, m, n = [], [], [], [], [], [], [], [], [], [], [], []

    for l in input:
        binary = list(l)
        a += binary[0]
        b += binary[1]
        c += binary[2]
        d += binary[3]
        e += binary[4] 
        g += binary[5]
        h += binary[6]
        i += binary[7]
        j += binary[8]
        k += binary[9]
        m += binary[10]
        n += binary[11]

    gamma = Counter(a).most_common()[0][0] + Counter(b).most_common()[0][0] + Counter(c).most_common()[0][0] + Counter(d).most_common()[0][0] + Counter(e).most_common()[0][0] + Counter(g).most_common()[0][0] + Counter(h).most_common()[0][0] + Counter(i).most_common()[0][0] + Counter(j).most_common()[0][0] + Counter(k).most_common()[0][0] + Counter(m).most_common()[0][0] + Counter(n).most_common()[0][0]
    epsilon = Counter(a).most_common()[-1][0] + Counter(b).most_common()[-1][0] + Counter(c).most_common()[-1][0] + Counter(d).most_common()[-1][0] + Counter(e).most_common()[-1][0] + Counter(g).most_common()[-1][0] + Counter(h).most_common()[-1][0] + Counter(i).most_common()[-1][0] + Counter(j).most_common()[-1][0] + Counter(k).most_common()[-1][0] + Counter(m).most_common()[-1][0] + Counter(n).most_common()[-1][0]
    print(f'Power Consumption: {int(gamma, 2) * int(epsilon, 2)}')


PowerConsumption()
