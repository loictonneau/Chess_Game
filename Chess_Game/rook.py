from Chess_Game import pieces

class Rook(pieces.Piece):

    def __init__(self,type,row,column,color):
        super().__init__(type, row, column, color)

    def get_available_moves(self,row,column,board):
        self.clear_available_move()

        for row_down in range(row+1,len(board[0])):
            if board[row_down][column] == 0:
                self.availables_moves.append((row_down, column))
            else:
                piece = board[row_down][column]
                if piece.color != self.color:
                    self.availables_moves.append((row_down, column))
                    break
                else:
                    break

        for row_up in range(row-1,-1,-1):

            if board[row_up][column] == 0:
                self.availables_moves.append((row_up, column))
            else:
                piece = board[row_up][column]
                if piece.color != self.color:
                    self.availables_moves.append((row_up, column))
                    break
                else:
                    break

        for column_right in range(column+1,len(board)):

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
        return self.availables_moves

    def display(self):
        if self.color=="white":
            return 't'
        elif self.color=="black":
            return 'T'