import numpy as np


class Board:
    def __init__(self, canvas, disks, disk_color):
        self.canvas = canvas
        self.disks = disks
        self.disk_color = disk_color
        self.grid = np.zeros((7, 6), dtype=int)

    def eval(self, player):
        # TODO
        # Nombre d'alignements de 2, 3 pourrait être intéressant à prendre en compte
        # avec + de reward pour 3 > 2
        return 0

    def copy(self):
        new_board = Board(self.canvas, self.disks, self.disk_color)
        new_board.grid = np.array(self.grid, copy=True)
        return new_board

    def reinit(self):
        self.grid.fill(0)
        for i in range(7):
            for j in range(6):
                self.canvas.itemconfig(self.disks[i][j], fill=self.disk_color[0])

    def get_possible_moves(self):
        possible_moves = list()
        if self.grid[3][5] == 0:
            possible_moves.append(3)
        for shift_from_center in range(1, 4):
            if self.grid[3 + shift_from_center][5] == 0:
                possible_moves.append(3 + shift_from_center)
            if self.grid[3 - shift_from_center][5] == 0:
                possible_moves.append(3 - shift_from_center)
        return possible_moves

    def add_disk(self, column, player, update_display=True):
        for j in range(6):
            if self.grid[column][j] == 0:
                break
        self.grid[column][j] = player
        if update_display:
            self.canvas.itemconfig(self.disks[column][j], fill=self.disk_color[player])

    def column_filled(self, column):
        return self.grid[column][5] != 0

    def check_victory(self):
        # Horizontal alignment check
        for line in range(6):
            for horizontal_shift in range(4):
                if (
                    self.grid[horizontal_shift][line]
                    == self.grid[horizontal_shift + 1][line]
                    == self.grid[horizontal_shift + 2][line]
                    == self.grid[horizontal_shift + 3][line]
                    != 0
                ):
                    return True
        # Vertical alignment check
        for column in range(7):
            for vertical_shift in range(3):
                if (
                    self.grid[column][vertical_shift]
                    == self.grid[column][vertical_shift + 1]
                    == self.grid[column][vertical_shift + 2]
                    == self.grid[column][vertical_shift + 3]
                    != 0
                ):
                    return True
        # Diagonal alignment check
        for horizontal_shift in range(4):
            for vertical_shift in range(3):
                if (
                    self.grid[horizontal_shift][vertical_shift]
                    == self.grid[horizontal_shift + 1][vertical_shift + 1]
                    == self.grid[horizontal_shift + 2][vertical_shift + 2]
                    == self.grid[horizontal_shift + 3][vertical_shift + 3]
                    != 0
                ):
                    return True
                elif (
                    self.grid[horizontal_shift][5 - vertical_shift]
                    == self.grid[horizontal_shift + 1][4 - vertical_shift]
                    == self.grid[horizontal_shift + 2][3 - vertical_shift]
                    == self.grid[horizontal_shift + 3][2 - vertical_shift]
                    != 0
                ):
                    return True
        return False
