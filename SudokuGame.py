from SudokuBoard import SudokuBoard, INDEXES_PAIRS, get_random_indexes

# CONSTANTS

NUMBER_OF_ROWS = 9
NUMBER_OF_COLUMNS = 9


class SudokuGame:
    def __init__(self):
        self.board = SudokuBoard()
        self.playing_board = SudokuBoard()
        # testing
        self.board.fill_board()
        pass

    def set_play_board(self, number_of_filled_cells=36):
        """gets a number of cells to reveal and sets the playing borad accordingly using the solved board """
        cells_indexes = get_random_indexes(number_of_filled_cells)
        for index_pair in INDEXES_PAIRS:
            if index_pair in cells_indexes:
                self.playing_board.board[index_pair[0]][index_pair[1]] = self.board.board[index_pair[0]][index_pair[1]]

    def is_game_over(self):
        """checks if playing board is full and returns True or False accordingly"""
        for row in range(NUMBER_OF_ROWS):
            for col in range(NUMBER_OF_COLUMNS):
                if self.playing_board.board[row][col] == 0:
                    return False

        return True
