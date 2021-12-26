class Board:
    def __init__(self, board):
        self.rows = [[*row] for row in board]
        self.columns = [[*col] for col in zip(*board)]
        self.resultColumns = [[0] * 5 for _ in range(len(board))]
        self.resultRows = [[0] * 5 for _ in range(len(board))]

    def isRowWinning(self):
        for row in self.resultRows:
            if row == [1, 1, 1, 1, 1]:
                return True

    def isColumnWinning(self):
        for column in self.resultColumns:
            if column == [1, 1, 1, 1, 1]:
                return True

    def scoreOfWinner(self):
        score = 0
        for i, row in enumerate(self.resultRows):
            for j, el in enumerate(row):
                if el == 0:
                    score += self.rows[i][j]
        return score


def findWinner(boards, numbers):
    for number in numbers:
        for board in boards:
            for j, row in enumerate(board.rows):
                for k, el in enumerate(row):
                    if el == number:
                        board.resultRows[j][k] = 1
                        board.resultColumns[k][j] = 1
                        if board.isRowWinning() or board.isColumnWinning():
                            return board, number


def findLastWinner(boards):
    for i in range(len(boards)):
        winner = findWinner(boards, numbers)
        boards.remove(winner[0])
    return winner


def finalScore(boardScore, winningNumber):
    return boardScore * winningNumber


numbers, *boards = open('input.txt').read().split('\n\n')
numbers = [int(number) for number in numbers.split(',')]
boards = [board.split('\n') for board in boards]
boards = [[[*map(int, row.split())] for row in board] for board in boards]
boards = [Board(board) for board in boards]

firstWinner, winningNumber = findWinner(boards, numbers)
lastWinner, lastWinningNumber = findLastWinner(boards)
print("Output of the second part: ", finalScore(firstWinner.scoreOfWinner(), winningNumber))
print("Output of the second part: ", finalScore(lastWinner.scoreOfWinner(), lastWinningNumber))
