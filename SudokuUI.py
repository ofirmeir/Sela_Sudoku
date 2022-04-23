from tkinter import Tk, Label, Entry, Button


# create conversion method
def btn_clicked():
    miles = int(entry_text.get())
    km = miles * 1.6
    label_km_value["text"] = f"{km:.2f}"


# create the window
window = Tk()
window.title("Sela Sudoku")
window.config(padx=100, pady=50)


# create 81 Entry widget
for row in range(9):
    for col in range(1, 10):
        entry_text = Entry(width=7)
        entry_text["text"] = "0"
        entry_text.grid(row=row, column=col)
        if row == 0 and col == 1:
            entry_text.focus()

# create check button
btn_check = Button(command=btn_clicked)
btn_check["text"] = "Check"
btn_check.grid(row=10, column=8)

# create check button
btn_new_board = Button(command=btn_clicked)
btn_new_board["text"] = "New"
btn_new_board.grid(row=10, column=9)

# hold window active
window.mainloop()


class SudokuError(Exception):
    pass




