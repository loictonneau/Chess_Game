from Chess_Game import pieces

class Queen(pieces.Piece):

    def __init__(self, type, row, column, color):
        super().__init__(type, row, column, color)

    def get_available_moves(self, row, column, board):  # connaitre le coup possible du pion
        self.clear_available_move()

        for row_down in range(row + 1, len(board[0])):
            if board[row_down][column] == 0:
                self.availables_moves.append((row_down, column))
            else:
                piece = board[row_down][column]
                if piece.color != self.color:
                    self.availables_moves.append((row_down, column))
                    break
                else:
                    break

        for row_up in range(row - 1, -1, -1):

            if board[row_up][column] == 0:
                self.availables_moves.append((row_up, column))
            else:
                piece = board[row_up][column]
                if piece.color != self.color:
                    self.availables_moves.append((row_up, column))
                    break
                else:
                    break

        for column_right in range(column + 1, len(board)):

            if board[row][column_right] == 0:
                self.availables_moves.append((row, column_right))
            else:
                piece = board[row][column_right]
                if piece.color != self.color:
                    self.availables_moves.append((row, column_right))
                    break
                else:
                    break

        for column_left in range(column - 1, -1, -1):

            if board[row][column_left] == 0:
                self.availables_moves.append((row, column_left))
            else:
                piece = board[row][column_left]
                if piece.color != self.color:
                    self.availables_moves.append((row, column_left))
                    break
                else:
                    break

        row_i = row + 1
        column_i = column + 1
        while row_i < len(board[0]) and column_i < len(board):
            if board[row_i][column_i] == 0:
                self.availables_moves.append((row_i, column_i))
                row_i += 1
                column_i += 1
            else:
                piece = board[row_i][column_i]
                if piece.color != self.color:
                    self.availables_moves.append((row_i, column_i))
                    break
                else:
                    break

        row_i = row - 1
        column_i = column - 1
        while row_i >= 0 and column_i >= 0:
            if board[row_i][column_i] == 0:
                self.availables_moves.append((row_i, column_i))
                row_i -= 1
                column_i -= 1
            else:
                piece = board[row_i][column_i]
                if piece.color != self.color:
                    self.availables_moves.append((row_i, column_i))
                    break
                else:
                    break

        row_i = row + 1
        column_i = column - 1
        while row_i < len(board[0]) and column_i >= 0:
            if board[row_i][column_i] == 0:
                self.availables_moves.append((row_i, column_i))
                row_i += 1
                column_i -= 1
            else:
                piece = board[row_i][column_i]
                if piece.color != self.color:
                    self.availables_moves.append((row_i, column_i))
                    break
                else:
                    break

        row_i = row - 1
        column_i = column + 1
        while row_i >= 0 and column_i < len(board):
            if board[row_i][column_i] == 0:
                self.availables_moves.append((row_i, column_i))
                row_i -= 1
                column_i += 1
            else:
                piece = board[row_i][column_i]
                if piece.color != self.color:
                    self.availables_moves.append((row_i, column_i))
                    break
                else:
                    break

        return self.availables_moves

    def display(self):
        if self.color=="white":
            return 'd'
        elif self.color=="black":
            return 'D'