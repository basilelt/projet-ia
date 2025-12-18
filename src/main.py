import tkinter as tk
from tkinter import ttk

from Connect4 import Connect4


if __name__ == "__main__":
    disk_color = ["white", "red", "orange"]
    disks = list()

    player_type = ["human"]
    for i in range(42):
        player_type.append("AI: alpha-beta level " + str(i + 1))

    # Graphical settings
    width = 700
    row_width = width // 7
    row_height = row_width
    height = row_width * 6
    row_margin = row_height // 10

    window = tk.Tk()
    window.title("Connect 4")
    canvas1 = tk.Canvas(window, bg="blue", width=width, height=height)

    # Drawing the grid
    for i in range(7):
        disks.append(list())
        for j in range(5, -1, -1):
            disks[i].append(
                canvas1.create_oval(
                    row_margin + i * row_width,
                    row_margin + j * row_height,
                    (i + 1) * row_width - row_margin,
                    (j + 1) * row_height - row_margin,
                    fill="white",
                )
            )

    canvas1.grid(row=0, column=0, columnspan=2)

    information = tk.Label(window, text="")
    information.grid(row=1, column=0, columnspan=2)

    label_player1 = tk.Label(window, text="Player 1: ")
    label_player1.grid(row=2, column=0)
    combobox_player1 = ttk.Combobox(window, state="readonly")
    combobox_player1.grid(row=2, column=1)

    label_player2 = tk.Label(window, text="Player 2: ")
    label_player2.grid(row=3, column=0)
    combobox_player2 = ttk.Combobox(window, state="readonly")
    combobox_player2.grid(row=3, column=1)

    combobox_player1["values"] = player_type
    combobox_player1.current(0)
    combobox_player2["values"] = player_type
    combobox_player2.current(6)

    game = Connect4(information, canvas1, combobox_player1, combobox_player2, row_width, window, disks, disk_color)

    button2 = tk.Button(window, text="New game", command=game.launch)
    button2.grid(row=4, column=0)

    button = tk.Button(window, text="Quit", command=window.destroy)
    button.grid(row=4, column=1)

    # Mouse handling
    canvas1.bind("<Button-1>", game.click)

    window.mainloop()
