from os import path
import unittest
from pathlib import Path
import context
from advent2021 import day15
from advent2021.utils import Timer

THIS_DIR = Path(__file__).parent

class Fixtures():
    def __init__(self):
        self.samplechitons = None
    
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
        with Timer():
            paths = day15.walk(chitons)
        print(f'paths: {len(paths)}')
        shortestpath = day15.shortest(paths, chitons)
        self.assertEqual(40, shortestpath[0])

    def test_walkfaster(self):
        chitons = fixtures.sample()
        with Timer():
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
        chitons = fixtures.sample()
        endx = len(chitons[0]) - 1
        endy = len(chitons) - 1      
        with Timer():
            winner = day15.astar(chitons, (0,0), (endx,endy), day15.manhattan)
        self.assertEqual(40, winner)






