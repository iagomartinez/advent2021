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
        if p1 >= 1000:
            loser = p2
            break
        elif p2 >= 1000:
            loser = p1
            break
    return timesrolled, loser

def quantumgame(positions, scores, universes, player):
    p1,p2 = scores
    if p1>=21:
        return universes,0
    elif p2>=21:
        return 0,universes
    wins = [0,0]
    for moves,times in [(3,1), (4,3), (5,6), (6,7), (7,6), (8,3), (9,1)]:
        newpositions = list(positions)
        newpositions[player] = ((positions[player] + moves - 1) % 10) + 1
        newscores = list(scores)
        newscores[player] += newpositions[player]
        w1,w2 = quantumgame(newpositions, newscores, universes * times, not player)
        wins[0] += w1
        wins[1] += w2
    return tuple(wins)


def main():
    print('----------- day21 -----------')
    timesrolled, loser = game([9,4], deterministicroll())
    print(f'For first ⭐: times rolled {timesrolled}, losing score {loser}, solution: {timesrolled*loser}')

    w1, w2 = quantumgame([9,4],[0,0],1,0)
    print(f'For ⭐⭐: scores {w1,w2}, winning universes {max(w1,w2)}')

if __name__ == '__main__':
    sys.exit(main())