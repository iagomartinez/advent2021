import sys
from pathlib import Path
from functools import reduce
from collections import Counter

THIS_DIR = Path(__file__).parent

def readbits(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        rows = []
        for line in f:
            bits = []
            for c in line.rstrip():
                bits.append(int(c))
            rows.append(bits)
    print(f'read {len(rows)} rows, each with {len(rows[0])} bits')
    return rows

#   Thanks to https://www.geeksforgeeks.org/python-binary-list-to-integer/    
def to_number(bitrow):
    res = 0
    for ele in bitrow:
        res = (res << 1) | ele
    return res

def countbits(report):
    size = reduce(lambda l0, l1: max(l0,len(l1)), report, 0)
    counters = {i:Counter([0,1]) for i in range(size)}

    for bitrow in report:
        for i,b in enumerate(bitrow):
            counters[i][b] += 1
    return counters

def computerates(counters):
    gamma = []
    epsilon = []
    for i in counters.keys():
        gamma.append(counters[i].most_common()[0][0])
        epsilon.append(counters[i].most_common()[1][0])
    return to_number(gamma), to_number(epsilon)

def main():
    file = THIS_DIR.parent / 'data/day3.txt'
    report = readbits(file)

    counters = countbits(report)
    gamma, epsilon = computerates(counters)

    print('----------- day3 -----------')
    print(f'For first ⭐: gamma:{gamma}, epsilon:{epsilon}, power consumption: {gamma*epsilon}')


if __name__ == '__main__':
    sys.exit(main())