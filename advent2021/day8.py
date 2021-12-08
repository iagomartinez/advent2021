import sys
from pathlib import Path
THIS_DIR = Path(__file__).parent
import re
from functools import reduce

def parsepattern(pattern):
    print(pattern)
    m = re.match(r'[^|]*[|]\s(?P<p1>[a-g]{1,})\s(?P<p2>[a-g]{1,})\s(?P<p3>[a-g]{1,})\s(?P<p4>[a-g]{1,})', pattern)
    return [m.group('p1'),m.group('p2'),m.group('p3'),m.group('p4')]

def countuniquedigits(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        all_patterns = [pattern for line in f for pattern in parsepattern(line.rstrip())]

    digitcounts = {2,4,3,7}
    return reduce(lambda tot,nextp: tot + 1 if nextp in digitcounts else tot, list(map(lambda p: len(p), all_patterns)),0)

def main():
    print('----------- day8 -----------')
    file = THIS_DIR.parent / 'data/day8.txt'
    print(f'For first ⭐: {countuniquedigits(file)} unique digits')

if __name__ == '__main__':
    sys.exit(main())