class TicTacToe():
    def __init__(self):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def DrawBoard(self):
        print(" %c | %c | %c " % (self.board[1], self.board[2], self.board[3]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[4], self.board[5], self.board[6]))
        print("___|___|___")
        print(" %c | %c | %c " % (self.board[7], self.board[8], self.board[9]))

    def Update_cell(self, cell_no, player):
        self.board[cell_no] = ""
        self.board[cell_no] = player

    def is_wins(self, player):
        if self.board[1] == player and self.board[2] == player and self.board[3] == player:
            return True
        elif self.board[4] == player and self.board[5] == player and self.board[6] == player:
            return True
        elif self.board[7] == player and self.board[8] == player and self.board[9] == player:
            return True
        elif self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        elif self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        elif self.board[3] == player and self.board[6] == player and self.board[9] == player:
            return True
        elif self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        elif self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True

        return False


t1 = TicTacToe()
t1.DrawBoard()

while True:

    X_choice = int(input("\nX) Enter the position between [1-9] where you want to mark : "))
    t1.Update_cell(X_choice, "X")
    t1.DrawBoard()
    if t1.is_wins("X"):
        print("\n X win")
        break
    o_choice = int(input("\no) Enter the position between [1-9] where you want to mark : "))
    t1.Update_cell(o_choice, "o")
    t1.DrawBoard()
    if t1.is_wins("o"):
        print("\n o win")
        break



