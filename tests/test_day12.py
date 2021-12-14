import sys
import unittest
from pathlib import Path
THIS_DIR = Path(__file__).parent

def buildgraph(input):
    nodes = dict()
    for connection in input:
        l,r = connection.split('-')
        if l in nodes:
            nodes[l] = nodes[l] | {r}
        else:
            nodes[l] = {r}
        if r in nodes:
            nodes[r] = nodes[r] | {l}
        else:
            nodes[r] = {l}
    return nodes

def visit(caves, verbose=True):
    def visit_inner(node, path, visited, verbose):
        if verbose:
            print(f'n: {node}, p:{path}, v:{visited}')
        paths = []
        if node == 'end':
            paths.append(path + (node,))
            return paths
        neighbours = caves[node]
        
        vis = {node, *visited} if node.islower() else visited
        not_visited = neighbours - vis
        
        if not not_visited:
            if verbose:
                print(f'pruned path {path}')
        if verbose:
            print(f'visited: {visited}')
        for cave in not_visited:
            paths.extend(visit_inner(cave, path + (node,), vis,verbose))
        return paths
    return visit_inner('start',(),set(),verbose)

def parsefile(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        return [l.rstrip() for l in f]

class Tests(unittest.TestCase):
    def test_buildgraph(self):
        input = ['start-A', 'start-b']
        nodes = buildgraph(input)
        self.assertCountEqual(['start', 'A', 'b'], nodes.keys())        
        self.assertCountEqual({'A', 'b'}, nodes['start'])

    def test_walk(self):
        input = ['start-A','start-B', 'B-end', 'A-end']
        caves = buildgraph(input)
        paths = visit(caves)
        print(paths)
        self.assertEqual(2, len(paths))     

    def test_lists(self):
        el = 'start'
        node = ['A','end']
        self.assertCountEqual(['start', 'A', 'end'], [el, *node])

    def test_smallsample(self):
        file = THIS_DIR.parent / 'data/day12_small.txt'        
        lines = parsefile(file)
        self.assertEqual(7, len(lines))
        caves = buildgraph(lines)
        print(caves)

        paths = visit(caves)
        print(paths)
        self.assertEqual(10, len(paths))

    def test_largesample(self):
        file = THIS_DIR.parent / 'data/day12_large.txt'
        caves = buildgraph(parsefile(file))
        print(caves)
        paths = visit(caves,False)
        print(paths)
        self.assertEqual(226, len(paths))    

    def test_day12_star1(self):
        file = THIS_DIR.parent / 'data/day12.txt'
        paths = visit(buildgraph(parsefile(file)),False)
        print(f'For first ⭐: {len(paths)} paths')
        self.assertTrue(True)
        
