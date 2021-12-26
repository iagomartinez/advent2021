import sys
import unittest
from pathlib import Path
THIS_DIR = Path(__file__).parent

def readfile(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        return [[int(i) for i in list(l.rstrip())] for l in f]

def findneighbours(point, lines):
    x,y = point
    if x > 0:
        yield (x-1,y)
    if x < len(lines[0])-1:
        yield (x+1, y)
    if y > 0:
        yield (x,y-1)
    if y < len(lines)-1:
        yield(x,y+1)

def islowpoint(point, lines):
    x,y = point
    value = lines[y][x]
    neighbours = findneighbours(point, lines)
    return all(map(lambda point: value < lines[point[1]][point[0]], neighbours))

def findlowpoints(lines):
    lowpoints = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if islowpoint((x,y), lines):
                lowpoints.add((x,y))

    totalrisk = sum([1+lines[y][x] for x,y in lowpoints])
    return totalrisk,lowpoints


class Tests(unittest.TestCase):
    def test_dayn(self):
        file = THIS_DIR.parent / 'data/day9_sample.txt'
        lines = readfile(file)
        self.assertEqual(5, len(lines))
        self.assertCountEqual([2,1,9,9,9,4,3,2,1,0],lines[0])

    def test_findneighbours(self):
        file = THIS_DIR.parent / 'data/day9_sample.txt'
        lines = readfile(file)
        testcases = [[(0,0), [(0,1),(1,0)]],
                    [(1,0),[(0,0), (1,1),(2,0)]],
                    [(9,0),[(8,0),(9,1)]],
                    [(1,1),[(1,0),(0,1),(2,1),(1,2)]],
                    [(0,4),[(0,3),(1,4)]],
                    [(9,4),[(8,4),(9,3)]]]
        for point,output in testcases:
            with self.subTest(msg=f'testing point {point}'):
                neighbours = findneighbours(point, lines)
                self.assertCountEqual(output, neighbours)
    
    def test_islowpoint(self):
        file = THIS_DIR.parent / 'data/day9_sample.txt'
        lines = readfile(file)
        point = (1,0)
        self.assertTrue(islowpoint(point, lines))

    def test_sample(self):
        file = THIS_DIR.parent / 'data/day9_sample.txt'
        lines = readfile(file)
        totalrisk, lowpoints = findlowpoints(lines)
        self.assertEqual(4, len(lowpoints))
        self.assertCountEqual([(1,0),(9,0),(2,2),(6,4)], lowpoints)
        self.assertEqual(15, totalrisk)

    def test_part1(self):
        file = THIS_DIR.parent / 'data/day9.txt'
        lines = readfile(file)
        totalrisk, _ = findlowpoints(lines)
        print(f'For first ⭐: total risk {totalrisk}')

        