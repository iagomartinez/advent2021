from os import times
import sys
from pathlib import Path
THIS_DIR = Path(__file__).parent

def deterministicroll(start = 1):
    roll = start
    def inner():
        nonlocal roll        
        current = roll
        roll = (roll % 100) + 1
        print(current,end=',')
        return current 
    return inner

class Board():
    def __init__(self, positions):
        self.__positions = list(positions)
        self.__scores = [0,0]
        self.player = 0
    
    def play(self, moves):
        newposition = ((self.__positions[self.player] + moves - 1) % 10) + 1
        self.__scores[self.player] += newposition
        self.__positions[self.player] = newposition
        self.player = not self.player

    def scores(self):
        return tuple(self.__scores)
    
    def positions(self):
        return tuple(self.__positions) 

def game(startpositions, roll):
    board = Board(tuple(startpositions))
    timesrolled = 0
    while True:
        moves = sum([roll(),roll(),roll()])
        timesrolled += 3
        board.play(moves)
        p1,p2 = board.scores()     
        print(f'scores after {timesrolled} rolls: {p1,p2}')       
        if p1 >= 1000:
            loser = p2
            break
        elif p2 >= 1000:
            loser = p1
            break
    return timesrolled, loser

def main():
    print('----------- day21 -----------')
    timesrolled, loser = game([9,4], deterministicroll())
    print(f'For first ⭐: times rolled {timesrolled}, losing score {loser}, solution: {timesrolled*loser}')


if __name__ == '__main__':
    sys.exit(main())