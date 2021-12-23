import sys
import unittest
from pathlib import Path
import context
from advent2021.day21 import deterministicroll
from advent2021.day21 import Board
from advent2021.day21 import game
from advent2021.day21 import quantumgame


THIS_DIR = Path(__file__).parent       

class Tests(unittest.TestCase):
    def test_roll(self):        
        roll = deterministicroll(1)
        self.assertCountEqual([1,2], [roll(), roll()])

    def test_rollwraps(self):
        roll = deterministicroll(100)
        self.assertEqual([100,1], [roll(), roll()])
    
    def test_newboard(self):
        board = Board((4,8))
        self.assertEqual((0,0), board.scores())

    def test_turns(self):
        board = Board((4,8))
        board.play(1)
        self.assertEqual((5,0), board.scores())
        self.assertEqual((5,8), board.positions())

        board.play(1)
        self.assertEqual((5,9), board.scores())
        self.assertEqual((5,9), board.positions())
        
    def test_boardwraps(self):
        board = Board((10,1))
        board.play(1)
        self.assertEqual((1,0), board.scores())
        self.assertEqual((1,1), board.positions())

    def test_positionat10(self):
        board = Board((8,1))
        board.play(2)
        self.assertEqual((10,1), board.positions())

    def test_game(self):
        timesrolled,loser = game((4,8), deterministicroll())        
        self.assertEqual(993, timesrolled)
        self.assertEqual(745,loser)

    def test_quantumgame(self):
        w1, w2 = quantumgame([4,8],[0,0],1,0)
        print(w1,w2)
        self.assertEqual(444356092776315, w1)