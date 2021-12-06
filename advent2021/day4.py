import sys
from pathlib import Path
THIS_DIR = Path(__file__).parent
import re

def readrow(line):
    line = line.rstrip().lstrip()
    m = re.match(r'(?P<n1>\d{1,2})\s{1,2}(?P<n2>\d{1,2})\s{1,2}(?P<n3>\d{1,2})\s{1,2}(?P<n4>\d{1,2})\s{1,2}(?P<n5>\d{1,2})', line)
    numbers = [int(m.group('n1')),int(m.group('n2')),int(m.group('n3')),int(m.group('n4')),int(m.group('n5'))]
    return numbers

def buildindex(boards):
    index = {}
    #for i, board in enumerate(boards):
    for i, board in boards.items():
        boardindex = []
        for line in board:
            boardindex.append([set(line), sum(line)])

        for col in range(5):
            column = [board[row][col] for row in range(5)]
            boardindex.append([set(column), sum(column)])
        index[i] = boardindex
    return index

def readnumbers(file):
    with open(file, 'r', newline='', encoding='utf-8') as f:
        number_order = [int(d) for d in f.readline().rstrip().split(',')]
        boards = {}
        board_id = 0 
        while True:
            board = []      
            if not f.readline():
                break
            for _ in range(5):
                numbers = readrow(f.readline())
                board.append(numbers)
            boards[board_id] = board
            board_id += 1
    return number_order, boards

def drawnumbers(number_order, index):
    last_draw = None
    for draw in number_order:

        for i, boardindex in index.items():
            for line in boardindex:
                if draw in line[0]:
                    print(f'MATCH {draw}')
                    line[1] -= draw
                if line[1] == 0:
                    last_draw = draw
                    winning_board = i
                    print("BINGO!!")
                    break
            if last_draw:
                break
        if last_draw:
            break
    
    score = sum([line[1] for line in index[winning_board]][0:5]) * last_draw
    return last_draw, winning_board, score

def main():
    print('----------- day4 -----------')

    file = THIS_DIR.parent / 'data/day4.txt'
    number_order, boards = readnumbers(file)
    index = buildindex(boards)
    assert(len(index) == 100)
    _, winning_board, score = drawnumbers(number_order, index)


    print(f'For first ⭐: winning board:{winning_board}, score: {score}')


if __name__ == '__main__':
    sys.exit(main())