"""
Class representing a generic sudoku board to which numbers can be added and removed from.
Will perform integrity checks on additions and reject them if they are invalid using constraints
"""
class Board:
    values = []
    length = 0
    width = 0
    subsquareLength = 0
    subsquareWidth = 0

    def __init__(self):
        self.length = 9
        self.width = 9
        self.subsquareLength = 3
        self.subsquareWidth = 3
        self.initEmptyValues()


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
