import sys
from pathlib import Path
from functools import reduce
THIS_DIR = Path(__file__).parent

def readlines(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        moves = []
        for line in f:
            c,v = line.split(' ')
            if c == 'forward':
                moves.append((int(v),0))
            elif c == 'backward':
                moves.append((-int(v),0))
            elif c == 'down':
                moves.append((0,int(v)))
            elif c == 'up':
                moves.append((0,-int(v)))
    return moves

def simpleposition(input):
    pos,depth = reduce(lambda p0,p1: (p0[0]+p1[0], p0[1]+p1[1]), input)
    print(f'final position:{pos}, depth:{depth}')
    return pos,depth

def positionwithaim(input):
    pos, depth, aim = 0,0,0
    for p,d in input:
        aim += d
        pos += p
        depth += p*aim
    print(f'final position:{pos}, aim:{aim}, depth:{depth}')
    return pos, depth

def main():
    print('----------- day2 -----------')
    
    input = readlines(THIS_DIR.parent / 'data/day2_p1.txt')
    pos,depth = simpleposition(input)
    print(f'For first ⭐: {pos*depth}')

    pos,depth = positionwithaim(input)
    print(f'For ⭐⭐: {pos*depth}')

if __name__ == '__main__':
    sys.exit(main())