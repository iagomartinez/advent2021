from os import path
import unittest
from pathlib import Path
import context
from advent2021 import day15
#import advent2021
#from advent2021.utils import Timer

THIS_DIR = Path(__file__).parent

class Fixtures():
    def __init__(self):
        self.samplechitons = None
    
    def samplefilepath(self):
        return THIS_DIR.parent / 'data/day15_sample.txt'

    def fullfilepath(self):
        return THIS_DIR.parent / 'data/day15.txt'

    def sample(self):
        if self.samplechitons:
            return self.samplechitons
        file = THIS_DIR.parent / 'data/day15_sample.txt'
        self.samplechitons = day15.readchitons(file)
        return self.samplechitons

fixtures = Fixtures()

class Tests(unittest.TestCase):
    def test_dayn(self):        
        chitons = fixtures.sample()
        self.assertCountEqual([1,1,6,3,7,5,1,7,4,2], chitons[0])
        self.assertEqual(10, len(chitons))

    def test_walk(self):
        chitons = fixtures.sample()
        paths = day15.walk(chitons)
        print(f'paths: {len(paths)}')
        shortestpath = day15.shortest(paths, chitons)
        self.assertEqual(40, shortestpath[0])

    def test_walkfaster(self):
        chitons = fixtures.sample()
        paths = day15.walkfaster(chitons)
        print(f'paths: {len(paths)}')
        winner = day15.shortestv2(paths)
        self.assertEqual(40, winner[0])

    def test_manhattan(self):
        testdata = [((0,0), (1,1), 2), ((1,1), (0,0), 2)]
        for start, end, score in testdata:
            with self.subTest(f'testing {start}->{end}'):
                self.assertEqual(score, day15.manhattan(start, end))
        
    def test_astar(self):
        chitonmap = day15.ChitonMap(fixtures.samplefilepath())
        endx = chitonmap.maxx
        endy = chitonmap.maxy
        winner = day15.astar(chitonmap, (0,0), (endx,endy), day15.manhattan)
        self.assertEqual(315, winner)

    def test_mapposition(self):
        map = day15.ChitonMap(fixtures.samplefilepath())
        testcases = [[(0,0),(0,0)], [(10,1),(0,1)], [(1,1),(1,1)], [(49,0),(9,0)], [(0,49),(0,9)]]
        for input, output in testcases:
            with self.subTest(msg=f'parse pattern {input}:'):            
                self.assertEqual(output, map.mapposition(input))
    
    def test_maxxmaxy(self):
        map = day15.ChitonMap(fixtures.samplefilepath())
        self.assertEqual((49,49), (map.maxx, map.maxy))

    def test_risklevel(self):
        map = day15.ChitonMap(fixtures.samplefilepath())        
        testcases = [[(1,1),1,1],
        [(10,1),1,2],[(19,1),1,2],[(20,1),1,3], 
        [(29,1),1,3],[(30,1),1,4],[(39,1),1,4],[(40,1),1,5], 
        [(49,1),1,5],
        [(10,1),9,1], # 9 goes back to 1
        [(10,10),9,2],
        [(1,49),1,5],
        [(49,49),1,9]]
        for position,chitons,risk in testcases:
            with self.subTest(msg=f'testing {position}'):
                self.assertEqual(risk, map.risklevel(chitons, position))

    def test_maxx_y(self):
        map = day15.ChitonMap(fixtures.fullfilepath())
        self.assertEqual((499,499), (map.maxx, map.maxy))

    def test_bigmap(self):
        map = day15.ChitonMap(fixtures.fullfilepath())
        lowercorner = [   [(99,99),1], [(99,199),2],[(199,199),3],
                        [(199,99),2], [(199,199),3],
                        [(499,99),5], [(99,499),5], [(499,499),9]]
        for position, risk in lowercorner:
            with self.subTest(msg='chitonrisk of lower corner {position}, expected: {risk}'):
                self.assertEqual(risk, map.chitonrisk(position))

        valueofeight = [   [(97,99),8], [(197,99),9], [(297,99),1]]
        for position, risk in valueofeight:
            with self.subTest(msg='chitonrisk of start value 8 {position}, expected: {risk}'):
                self.assertEqual(risk, map.chitonrisk(position))                