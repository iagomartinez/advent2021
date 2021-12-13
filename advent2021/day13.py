import sys
from pathlib import Path
THIS_DIR = Path(__file__).parent
import re

def parsefile(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        points = []
        for line in f:
            if line.rstrip():
                points.append(parsepoint(line))
            else:
                break
        folds = []
        for line in f:
            folds.append(parsefold(line))
    
    return points, folds

def parsepoint(input):
    s = input.split(",")
    point = int(s[0]),int(s[1])
    return point

def parsefold(input):
    m = re.match(r'fold along y=(?P<foldline>\d{1,})', input)
    if m:
        return (0, int(m.group('foldline')))
    m = re.match(r'fold along x=(?P<foldline>\d{1,})', input)
    if m:
        return (int(m.group('foldline')), 0)
    return None

def foldpoints(points, foldline):
    return {fold(p,foldline) for p in points}

def fold(point, foldline):
    x, y = point
    foldx, foldy = foldline

    newpos = lambda pos, fold : pos if pos < fold else fold - (pos - fold)
    
    if (foldy):
        if y == foldy:
            return None
        return  x, newpos(y, foldy)
    if (foldx):
        if x == foldx:
            return None
        return  newpos(x, foldx), y
    raise 'unknown case' 

def main():
    print('----------- day13 -----------')
    file = THIS_DIR.parent / 'data/day13.txt'
    points, folds = parsefile(file)
    
    folded = foldpoints(points, folds[0])

    print(f'For first ⭐: {len(folded)}')

if __name__ == '__main__':
    sys.exit(main())