from threading import Thread
from queue import Queue
from Board import Board
import random as rnd


## Extrait du TP2 - Morpion
def max_value_ab(board, turn, alpha, beta, depth, max_player):
    if board.check_victory():
        return 1
    if depth == 0 or turn > 42 or not board.get_possible_moves():
        return 0
    possible_moves = board.get_possible_moves()
    value = float('-inf')
    opponent = 3 - max_player
    for move in possible_moves:
        updated_board = board.copy()
        updated_board.add_disk(move, max_player, update_display=False)
        value = max(value, min_value_ab(updated_board, turn + 1, alpha, beta, depth-1, max_player))
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value


## Extrait du TP2 - Morpion
def min_value_ab(board, turn, alpha, beta, depth, max_player):
    if board.check_victory():
        return -1
    if depth == 0 or turn > 42 or not board.get_possible_moves():
        return 0
    possible_moves = board.get_possible_moves()
    value = float('inf')
    opponent = 3 - max_player
    for move in possible_moves:
        updated_board = board.copy()
        updated_board.add_disk(move, opponent, update_display=False)
        value = min(value, max_value_ab(updated_board, turn + 1, alpha, beta, depth-1, max_player))
        if value <= alpha:
            return value
        beta = min(beta, value)
    return value


## Extrait du TP2 - Morpion
def alpha_beta_decision(board, turn, ai_level, queue, max_player):
    # # random move (to modify)
    # queue.put(
    #     board.get_possible_moves()[rnd.randint(0, len(board.get_possible_moves()) - 1)]
    # )
    # TODO

    possible_moves = board.get_possible_moves()
    best_move = possible_moves[0]
    best_value = float('-inf')
    alpha = float('-inf')
    beta = float('inf')
    for move in possible_moves:
        updated_board = board.copy()
        updated_board.add_disk(move, max_player, update_display=False)
        value = min_value_ab(updated_board, turn + 1, alpha, beta, ai_level, max_player)
        if value > best_value:
            best_value = value
            best_move = move
    queue.put(best_move)


class Connect4:
    def __init__(
        self,
        information,
        canvas1,
        combobox_player1,
        combobox_player2,
        row_width,
        window,
        disks,
        disk_color,
    ):
        self.information = information
        self.canvas1 = canvas1
        self.combobox_player1 = combobox_player1
        self.combobox_player2 = combobox_player2
        self.row_width = row_width
        self.window = window
        self.board = Board(canvas1, disks, disk_color)
        self.human_turn = False
        self.turn = 1
        self.players = (0, 0)
        self.ai_move = Queue()

    def current_player(self):
        return 2 - (self.turn % 2)

    def launch(self):
        self.board.reinit()
        self.turn = 0
        self.information["fg"] = "black"
        self.information["text"] = (
            "Turn "
            + str(self.turn)
            + " - Player "
            + str(self.current_player())
            + " is playing"
        )
        self.human_turn = False
        self.players = (
            self.combobox_player1.current(),
            self.combobox_player2.current(),
        )
        self.handle_turn()

    def move(self, column):
        if not self.board.column_filled(column):
            self.board.add_disk(column, self.current_player())
            self.handle_turn()

    def click(self, event):
        if self.human_turn:
            column = event.x // self.row_width
            self.move(column)

    def ai_turn(self, ai_level):
        Thread(
            target=alpha_beta_decision,
            args=(
                self.board,
                self.turn,
                ai_level,
                self.ai_move,
                self.current_player(),
            ),
        ).start()
        self.ai_wait_for_move()

    def ai_wait_for_move(self):
        if not self.ai_move.empty():
            self.move(self.ai_move.get())
        else:
            self.window.after(100, self.ai_wait_for_move)

    def handle_turn(self):
        self.human_turn = False
        if self.board.check_victory():
            self.information["fg"] = "red"
            self.information["text"] = (
                "Player " + str(self.current_player()) + " wins !"
            )
            return
        elif self.turn >= 42:
            self.information["fg"] = "red"
            self.information["text"] = "This a draw !"
            return
        self.turn = self.turn + 1
        self.information["text"] = (
            "Turn "
            + str(self.turn)
            + " - Player "
            + str(self.current_player())
            + " is playing"
        )
        if self.players[self.current_player() - 1] != 0:
            self.human_turn = False
            self.ai_turn(self.players[self.current_player() - 1])
        else:
            self.human_turn = True
