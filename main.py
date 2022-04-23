import tkinter.messagebox
from tkinter import *
from tkinter import Tk, Label, Entry, Button, Toplevel, Radiobutton, StringVar, END
from SudokuGame import SudokuGame

DIFFICULTY = 0
CELL_WIDTH = 4

RADIO_BTN_DIFFICULTY_SELECTION = {
    "Easy": 36,
    "Medium": 31,
    "Hard": 28
}

GAME = None


def btn_new_board_clicked(window):
    # open a difficulty selection window
    window.quit()
    difficulty_window.deiconify()


def validate(value, row, col):
    '''register'''
    global GAME
    try:
        int(value)
        if int(value) > 0 or int(value) <= 9:
            print(f'nice its a number: {value}, row: {row} col: {col} ')
            print('checking if it is a legal assignment')
            if GAME.playing_board.is_legal_assignment(int(row), int(col), int(value)):
                GAME.playing_board.board[int(row)][int(col)] = int(value)
                return True
            else:
                tkinter.messagebox.showwarning("Warning", "Illegal move")
    except Exception as e:
        print(e)
        if value == '':
            GAME.playing_board[row][col] = value
            return True
        else:
            return False
    return False


def on_invalid():
    print("damn")
    pass


def value_inserted(event):
    print("got it")
    print(event)
    pass


# create conversion method
def btn_clicked():
    pass


def start_game():
    global DIFFICULTY
    DIFFICULTY = selected_difficulty.get()
    open_game_window()


def open_game_window():
    global GAME
    # create the window
    game_window = Toplevel()
    game_window.title("Sela Sudoku")
    game_window.config(padx=100, pady=50)

    GAME = SudokuGame()
    GAME.set_play_board(DIFFICULTY)
    entries_list = []

    reg = game_window.register(validate)

    # create 81 Entry widget
    for row in range(9):
        for col in range(9):
            number_in_filled_board = GAME.playing_board.board[row][col]
            if number_in_filled_board != 0:
                v = StringVar(game_window, value=str(number_in_filled_board))
                entry_text = Entry(game_window,
                                   state='readonly',
                                   textvariable=v,
                                   width=CELL_WIDTH,
                                   bg='white',
                                   justify=CENTER)
            else:
                v = StringVar('')
                entry_text = Entry(game_window,
                                   textvariable=v,
                                   width=CELL_WIDTH,
                                   justify=CENTER
                                   )
                # v.(command=lambda: value_inserted(v.get(), row, col))
                # entry_text.bind('<Return>', value_inserted)
                entry_text.config(validate="key", validatecommand=(reg, '%P', row, col))

            entry_text.grid(row=row, column=col)
            entries_list.append(entry_text)

    # create new button
    btn_new_board = Button(game_window, command=game_window.destroy)
    btn_new_board["text"] = "New"
    btn_new_board.grid(row=10, column=9)


# program starts here
difficulty_window = Tk()
difficulty_window.geometry('200x250')
difficulty_window.title("New Game")

label_welcome = Label(difficulty_window, text='Choose the difficulty level: ')
label_welcome.grid(row=0, column=0)

selected_difficulty = IntVar()
row = 1
for (text, value) in RADIO_BTN_DIFFICULTY_SELECTION.items():
    btn_radio = Radiobutton(difficulty_window,
                            text=text,
                            value=value,
                            variable=selected_difficulty,
                            justify=RIGHT)
    btn_radio.grid(row=row, column=0, sticky='w')
    row += 1

DIFFICULTY = selected_difficulty.get()

btn_select = Button(difficulty_window,
                    text="Select",
                    command=start_game)
btn_select.grid(row=row, column=0)

# hold window active
difficulty_window.mainloop()
