"""
Class representing a generic sudoku board to which numbers can be added and removed from.
Will perform integrity checks on additions and reject them if they are invalid using constraints
"""
class Board:
    values = []
    length = 9
    width = 9
    subsquareLength = 3
    subsquareWidth = 3
    minValue = 1
    maxValue = 9

    def __init__(self, length = 9, width = 9, subsquareLength = 3, subsquareWidth = 3):
        self.length = length
        self.width = width
        self.subsquareLength = subsquareLength
        self.subsquareWidth = subsquareWidth
        assert length % subsquareLength == 0, 'length must be divisible by subsquareLength'
        assert width % subsquareWidth == 0, 'width must be divisible by subsquareWidth'
        self.initEmptyValues()
        self.maxValue = max(subsquareLength*subsquareWidth, length, width)

    def initEmptyValues(self):
        for i in range(0, self.length):
            row = []
            for j in range(0, self.width):
                row += [None]
            self.values += [row]
                
            
if __name__ == '__main__':
    board = Board()
    for x in board.values:
        for y in x:
            assert y is None, 'All values in an initial board should be None'
    board = Board(10, 8, 5, 2)
    assert board.maxValue == 10, 'Board should initialize the correct max value'
