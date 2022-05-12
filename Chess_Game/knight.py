from Chess_Game import pieces

class Knight(pieces.Piece):

    def __init__(self, type, row, column, color):
        super().__init__(type, row, column, color)

    def get_available_moves(self, row, column, board):  # connaitre le coup possible du pion
        self.clear_available_move()

        if row-2 >=0 and column+1 < len(board):
            if board[row-2][column+1] == " ":
                self.availables_moves.append((row - 2, column + 1))
            else:
                piece = board[row-2][column+1]
                if piece.color != self.color:
                    self.availables_moves.append((row - 2, column + 1))

        if row-2 >=0 and column-1 >=0:
            if board[row-2][column-1] == " ":
                self.availables_moves.append((row - 2, column - 1))
            else:
                piece = board[row-2][column-1]
                if piece.color != self.color:
                    self.availables_moves.append((row - 2, column - 1))

        if row+2 < len(board[0]) and column+1 < len(board):
            if board[row+2][column+1] == " ":
                self.availables_moves.append((row + 2, column + 1))
            else:
                piece = board[row+2][column+1]
                if piece.color != self.color:
                    self.availables_moves.append((row + 2, column + 1))

        if row+2 < len(board[0]) and column-1 >=0:
            if board[row+2][column-1] == " ":
                self.availables_moves.append((row + 2, column - 1))
            else:
                piece = board[row+2][column-1]
                if piece.color != self.color:
                    self.availables_moves.append((row + 2, column - 1))

        if row-1 >=0 and column+2 < len(board):
            if board[row-1][column+2] == " ":
                self.availables_moves.append((row - 1, column + 2))
            else:
                piece = board[row-1][column+2]
                if piece.color != self.color:
                    self.availables_moves.append((row - 1, column + 2))

        if row-1 >=0 and column-2 >=0:
            if board[row-1][column-2] == " ":
                self.availables_moves.append((row - 1, column - 2))
            else:
                piece = board[row-1][column-2]
                if piece.color != self.color:
                    self.availables_moves.append((row - 1, column - 2))

        if row+1 < len(board[0]) and column+2 < len(board):
            if board[row+1][column+2] == " ":
                self.availables_moves.append((row + 1, column + 2))
            else:
                piece = board[row+1][column+2]
                if piece.color != self.color:
                    self.availables_moves.append((row + 2, column + 1))

        if row+1 < len(board[0]) and column-2 >=0:
            if board[row+1][column-2] == " ":
                self.availables_moves.append((row + 2, column - 1))
            else:
                piece = board[row+1][column-2]
                if piece.color != self.color:
                    self.availables_moves.append((row + 1, column - 2))

        return self.availables_moves

    def display(self):
        if self.color=="white":
            return 'c'
        elif self.color=="black":
            return 'C'