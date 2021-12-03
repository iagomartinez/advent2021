import sys
from pathlib import Path
from functools import reduce
from collections import Counter

THIS_DIR = Path(__file__).parent

#   Counter helpers
most_common = lambda counter: counter.most_common()[0][0]
least_common = lambda counter: counter.most_common()[-1][0]

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
        gamma.append(most_common(counters[i]))
        epsilon.append(least_common(counters[i]))
    return to_number(gamma), to_number(epsilon)

def applycriteria(position, rows, criteria):
    if len(rows) == 0:
        raise RuntimeError('applycriteria got 0 rows')
    counters = countbits(rows)
    testvalue = criteria(counters[position])
    filtered = [row for row in rows if row[position] == testvalue]
    return filtered

def computerating(input, counters, criteria):
    for i in counters.keys():
        input = applycriteria(i, input, criteria)
        if len(input) == 1:
            break                
    return to_number(input[0])

def computelifesupportrates(input, counters):
    oxygen_criteria = lambda counter: 1 if counter[0] == counter[1] else most_common(counter)
    oxygen_rating = computerating(input,counters, oxygen_criteria)

    co2scrubber_criteria = lambda counter: 0 if counter[0] == counter[1] else least_common(counter)
    co2scrubber_rating = computerating(input,counters, co2scrubber_criteria)

    return oxygen_rating, co2scrubber_rating

def main():
    file = THIS_DIR.parent / 'data/day3.txt'
    report = readbits(file)

    counters = countbits(report)
    gamma, epsilon = computerates(counters)

    print('----------- day3 -----------')
    print(f'For first ⭐: gamma:{gamma}, epsilon:{epsilon}, power consumption: {gamma*epsilon}')

    oxygen_rating, co2scrubber_rating = computelifesupportrates(report, counters)
    print(f'For ⭐⭐: O2 generator rating:{oxygen_rating}, CO2 scrubber rating:{co2scrubber_rating}, life support: {oxygen_rating*co2scrubber_rating}')

if __name__ == '__main__':
    sys.exit(main())