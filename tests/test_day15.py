import sys
import unittest
from pathlib import Path
from math import floor, inf
from math import ceil
import context
from advent2021.utils import Timer

THIS_DIR = Path(__file__).parent

def readchitons(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        return [list(map(lambda x: int(x), list(line.rstrip()))) for line in f]

def walk(chitons, x=0, y=0):
    maxx = len(chitons[0]) - 1
    maxy = len(chitons) - 1      

    visited = 0

    def walk_inner(x,y, path):
        nonlocal visited
        paths = []
        if (x,y) == (maxx,maxy):
            paths.append((path))
            return paths
        if y < maxy:
            paths.extend(walk_inner(x, y+1, path + [(x,y)]))
        if x < maxx:
            paths.extend(walk_inner(x+1, y, path + [(x,y)]))
        visited += len(paths)
        return paths            
    paths = walk_inner(x,y,[]) 
    print(f'visited: {visited}')
    return paths

def walkfaster(chitons, x=0, y=0):
    maxx = len(chitons[0]) - 1
    maxy = len(chitons) - 1

    pathmap = dict()
    visited = 0
    pruned = 0

    addchitons = lambda count, x0, y0: count if x0==x and y0==y else count + chitons[y0][x0]

    def walk_inner(x,y, path, chitoncount):
        nonlocal visited
        nonlocal pruned
        paths = []
        if (x,y) == (maxx,maxy):
            chitoncount+=chitons[y][x]
            assert path is not None,"base case: path is None"
            paths.append((chitoncount, path))
            return paths
        currentmin = pathmap.get((x,y))
        if currentmin:
            (minchitons, minpath) = currentmin
            if minchitons < chitoncount:
                pruned +=1
                return paths
                
            else:
                pathmap[(x,y)] = (chitoncount, path)
        
        if y < maxy:    
            assert path is not None,f"{x}, {y}, {path} y<maxy: path is None"

            newpaths = walk_inner(x, y+1, path + [(x,y)], addchitons(chitoncount,x, y))
            if len(newpaths) > 0:                
                minpath = min(newpaths, key=lambda p:p[0])
                paths.append(minpath)
                currentmin = pathmap.get((x,y))
                if currentmin:
                    if minpath[0] < currentmin[0]:
                        pathmap[(x,y)] = minpath
                else:
                    pathmap[(x,y)] = minpath

                
        if x < maxx:
            assert path is not None,"x<maxx: path is None"
            newpaths = walk_inner(x+1, y, path + [(x,y)], addchitons(chitoncount,x, y))

            if len(newpaths) > 0:
                minpath = min(newpaths, key=lambda p:p[0])
                paths.append(minpath)

                currentmin = pathmap.get((x,y))
                if currentmin:
                    if minpath[0] < currentmin[0]:
                        pathmap[(x,y)] = minpath
                else:
                    pathmap[(x,y)] = minpath


        visited += len(paths)
        return paths        
    paths = walk_inner(x,y,[],0)
    print(f'visited: {visited}, pruned: {pruned}')
    return paths


def measure(paths, chitons):
    walks = []
    for path in paths:
        mapped = (sum(list(map(lambda pos: chitons[pos[1]][pos[0]],path))), path)
        walks.append(mapped)
    return sorted(walks,key=lambda t: t[0])

def shortest(paths, chitons):
    sortedwalks = measure(paths, chitons)
    return sortedwalks[0]

def shortestv2(paths):
    sortedwalks = sorted(paths, key=lambda p: p[0])
    return sortedwalks[0]

class Tests(unittest.TestCase):
    def test_dayn(self):        
        file = THIS_DIR.parent / 'data/day15_sample.txt'                
        chitoncounts = readchitons(file)
        self.assertCountEqual([1,1,6,3,7,5,1,7,4,2], chitoncounts[0])
        self.assertEqual(10, len(chitoncounts))

    def test_walk(self):
        file = THIS_DIR.parent / 'data/day15_sample.txt'
        chitons = readchitons(file)
        with Timer():
            paths = walk(chitons)
        print(f'paths: {len(paths)}')
        shortestpath = shortest(paths, chitons)
        self.assertEqual(40, shortestpath[0])

    def test_walkfaster(self):
        file =  THIS_DIR.parent / 'data/day15_sample.txt'        
        chitons = readchitons(file)
        
        with Timer():
            paths = walkfaster(chitons)
        print(f'paths: {len(paths)}')
        winner = shortestv2(paths)
        self.assertEqual(40, winner[0])

    # def test_first_star(self):
    #     file =  THIS_DIR.parent / 'data/day15.txt'
    #     with Timer():
    #         paths = walkfaster(readchitons(file))
    #     winner = shortestv2(paths)
    #     print(f'For first ⭐: shortest path is {winner[0]}')



