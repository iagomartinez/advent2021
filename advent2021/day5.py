import sys
from pathlib import Path
THIS_DIR = Path(__file__).parent
import re

def parsesegment(text):
    m = re.match(r'(?P<x0>\d{1,})\,(?P<y0>\d{1,})\s\->\s(?P<x1>\d{1,})\,(?P<y1>\d{1,})', text)
    x0,y0,x1,y1 = int(m.group('x0')), int(m.group('y0')), int(m.group('x1')), int(m.group('y1'))
    return x0,y0,x1,y1

def parsefile(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        return [parsesegment(line.rstrip()) for line in f]

def selectlines(coordinates):
    vert = [(x0,y0,x1,y1) for x0,y0,x1,y1 in coordinates if x0 == x1]
    hor = [(x0,y0,x1,y1) for x0,y0,x1,y1 in coordinates if y0 == y1]
    return hor, vert
    
def buildindex(coordinates):
    hor, vert = selectlines(coordinates)
    index = {}
    for x0,y,x1,_ in hor:
        for x in range(min(x0,x1), max(x0,x1) + 1):
            if (x,y) in index:
                index[(x,y)] += 1
            else:
                index[(x,y)] = 1
    
    for x,y0,_,y1 in vert:
        for y in range(min(y0,y1), max(y0,y1) + 1):
            if (x,y) in index:
                index[(x,y)] += 1
            else:
                index[(x,y)] = 1
    return index

def finddangerpoints(file):
    index = buildindex(parsefile(file))
    return [(x,y) for (x,y),coverage in index.items() if coverage >=2]

def main():
    print('----------- day5 -----------')
    dangerpoints = finddangerpoints(THIS_DIR.parent / 'data/day5.txt')
    print(f'For first ⭐: {len(dangerpoints)} danger points')

if __name__ == '__main__':
    sys.exit(main())