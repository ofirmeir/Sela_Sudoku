from random import choice, shuffle

NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
INDEXES_PAIRS = []


def get_indexes():
    """generate a list of indexes and shuffles it. helper method for backtracking"""
    global INDEXES_PAIRS
    for row in range(9):
        for col in range(9):
            INDEXES_PAIRS.append((row, col))
    # shuffle(INDEXES_PAIRS)


def get_all_indexes():
    return INDEXES_PAIRS


def get_random_indexes(number_of_indexes=36):
    """gets a number of random indexes and returns a list of random indexes of the board"""
    cells_indexes = []
    for i in range(number_of_indexes):
        found_new_index = False
        while not found_new_index:
            random_indexes = choice(INDEXES_PAIRS)
            if random_indexes not in cells_indexes:
                cells_indexes.append(random_indexes)
                found_new_index = True
    return cells_indexes


class SudokuBoard:
    def __init__(self):
        self.board = []
        self.__create_empty_board()
        pass

    def __create_empty_board(self):
        self.board = [[0 for i in range(9)] for _ in range(9)]

    def fill_board(self):
        get_indexes()
        self.__backtrack_fill_board(0)

    def __backtrack_fill_board(self, indexes_pair_idx):
        """fills the board with legal assignment using backtracking"""
        if indexes_pair_idx == 81:
            return True

        current_row = INDEXES_PAIRS[indexes_pair_idx][0]   # row idx
        current_column = INDEXES_PAIRS[indexes_pair_idx][1]  # col idx

        available_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        while len(available_numbers) > 0:
            # pick a number and try it on the board
            random_number = choice(available_numbers)
            if self.is_legal_assignment(current_row, current_column, random_number):
                # put it in the board and move on
                self.board[current_row][current_column] = random_number
                success = self.__backtrack_fill_board(indexes_pair_idx + 1)
                if success:
                    return True
                else:
                    # try a new number
                    self.board[current_row][current_column] = 0

            # leave the current number
            available_numbers.remove(random_number)

        # if we checked all numbers we initialize the spot and report back
        if len(available_numbers) == 0:
            self.board[current_row][current_column] = 0
            return

    def is_move_legal(self, number, available_positions):
        positions = available_positions
        random_position = choice(positions)
        random_number = choice(NUMBERS)
        positions.pop(random_position)

    def is_legal_assignment(self, row, col, number):
        """for a given cell indexes and a number, checks if the assignment is legal
        return True if legal or False otherwise."""
        a = self.__is_legal_row_assignment(row, number)
        b = self.__is_legal_column_assignment(col, number)
        c = self.__is_legal_box_assignment(row, col, number)
        return self.__is_legal_row_assignment(row, number) \
               and self.__is_legal_column_assignment(col, number) \
               and self.__is_legal_box_assignment(row, col, number)

    def select_random_indexes(self, difficulty_number):
        """selects a number of cells by their indexes and returns the list of indexes"""
        pass

    def __fill_board_with_random_indexes(self, difficulty_number):
        """fills the board with X cells according to the user's choice"""
        pass

    def __is_legal_row_assignment(self, row_idx, number):
        """checks if the number already exists in the row.
        return True if the assignment is legal or False otherwise"""
        return number not in self.board[row_idx]

    def __is_legal_column_assignment(self, col_idx, number):
        """checks if the number already exists in the column.
        return True if the assignment is legal or False otherwise"""
        return number not in self.__get_column(col_idx)

    def __is_legal_box_assignment(self, row_idx, col_idx, number):
        """checks if the number already exists in the related box.
        return True if the assignment is legal or False otherwise"""
        box_row_first_idx = int((row_idx // 3) * 3)
        box_col_first_idx = int((col_idx // 3) * 3)
        for r in range(box_row_first_idx, box_row_first_idx + 3):
            for c in range(box_col_first_idx, box_col_first_idx + 3):
                if self.board[r][c] == number:
                    return False
        return True

    def __get_column(self, i):
        """returns a list of column cells of column index i"""
        return [row[i] for row in self.board]
