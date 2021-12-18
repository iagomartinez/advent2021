from os import path
import sys
from pathlib import Path
from advent2021.utils import Timer

THIS_DIR = Path(__file__).parent

class ChitonMap():
    def __init__(self, file):
        with open(file, 'r', newline='', encoding='utf-8') as f:
            self._chitontile = [list(map(lambda x: int(x), list(line.rstrip()))) for line in f]
            self.__lenx = len(self._chitontile[0])
            self.__leny = len(self._chitontile)
            self.maxx = (self.__lenx * 5) - 1
            self.maxy = (self.__leny * 5) - 1

    def mapposition(self, pos):
        x,y = pos
        relativex = x % self.__lenx
        relativey = y % self.__leny
        return relativex, relativey

    def risklevel(self, chitonvalue, pos):
        x,y = pos
        extra_risk = x // self.__lenx + y // self.__leny
        chitonrisk = chitonvalue + extra_risk
        if chitonrisk > 9:
            chitonrisk -= 9
        return chitonrisk

    def chitonrisk(self, pos):
        x, y = self.mapposition(pos)
        assert x < self.__lenx, f'{x} >= {self.__lenx}'
        assert y < self.__leny, f'{y} >= {self.__leny}'
        return self.risklevel(self._chitontile[y][x], pos)

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
    pruned = set()

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
        if frozenset(path) in pruned:
            return paths
        currentmin = pathmap.get((x,y))
        if currentmin:
            (minchitons, minpath) = currentmin
            if minchitons < chitoncount:
                pruned.add(frozenset(path))
                return paths                
            else:
                pathmap[(x,y)] = (chitoncount, path)                
        if y < maxy:    
            assert path is not None,f"{x}, {y}, {path} y<maxy: path is None"
            newpaths = walk_inner(x, y+1, path + [(x,y)], addchitons(chitoncount,x, y))
            paths.extend(newpaths)

        if x < maxx:
            assert path is not None,"x<maxx: path is None"
            newpaths = walk_inner(x+1, y, path + [(x,y)], addchitons(chitoncount,x, y))
            paths.extend(newpaths)

        if len(paths) > 0:
            rankedpaths = sorted(paths, key=lambda p:p[0])
            minpath = rankedpaths[0]
            visited += len(paths)
            paths=[minpath]
            for _,p in rankedpaths[1:]:
                pruned.add(frozenset(p))
            currentmin = pathmap.get((x,y))
            if currentmin:
                if minpath[0] < currentmin[0]:
                    pathmap[(x,y)] = minpath
            else:
                pathmap[(x,y)] = minpath
        return paths        
    paths = walk_inner(x,y,[],0)
    print(f'visited: {visited}, pruned: {len(pruned)}')
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

def manhattan(current, goal):
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

#   Credit to https://www.geeksforgeeks.org/a-search-algorithm/ 
#   for the pseudocode that inspired this function 🙏
def astar(chitonmap, start, goal, h):
    openset = {start}
    camefrom = dict()
    gscore = {start: 0}
    fscore = {start:h(start, goal)}
    get_g = lambda pos: gscore.get(pos, 999)
    goalx,goaly = goal

    def find_neighbours(current):
        x,y = current
        if x < goalx:
            yield x+1, y
        if y < goaly:
            yield x, y+1

    while len(openset) > 0:
        current = min(openset, key=lambda pos: fscore[pos])
        if current == goal:
            return gscore[current]
        openset.remove(current)
        for neighbour in find_neighbours(current):
            xn, yn = neighbour
            tentativescore = get_g(current) + chitonmap.chitonrisk((xn,yn))            
            neighbourscore = get_g(neighbour)
            if tentativescore < neighbourscore:
                camefrom[neighbour] = current
                gscore[neighbour] = tentativescore
                fscore[neighbour] = tentativescore + h(neighbour, goal)
                if neighbour not in openset:
                    openset.add(neighbour)    
    raise 'failed to find a path!'

def main():
    file =  THIS_DIR.parent / 'data/day15.txt'
    print('----------- day15 -----------')
    with Timer():
        chitons = readchitons(file)
        endx = len(chitons[0]) - 1
        endy = len(chitons) - 1                  
        winner = astar(chitons, (0,0), (endx,endy), manhattan)
    print(f'For first ⭐: shortest path is {winner}')

if __name__ == '__main__':
    sys.exit(main())