from Chess_Game import  pieces

class Bishop(pieces.Piece):

    def __init__(self,type,row,column,color):
        super().__init__(type, row, column, color)

    def get_available_moves(self,row,column,board): #connaitre le coup possible du pion
        self.clear_available_move()

        row_i = row+1
        column_i = column+1
        while row_i <len(board[0]) and column_i<len(board):
            if board[row_i][column_i] == " ":
                self.availables_moves.append((row_i, column_i))
                row_i+=1
                column_i+=1
            else:
                piece = board[row_i][column_i]
                if piece.color != self.color:
                    self.availables_moves.append((row_i, column_i))
                    break
                else:
                    break

        row_i = row - 1
        column_i = column - 1
        while row_i >=0 and column_i >=0:
            if board[row_i][column_i] == " ":
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
        while row_i <len(board[0]) and column_i >=0:
            if board[row_i][column_i] == " ":
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
        while row_i >=0 and column_i < len(board):
            if board[row_i][column_i] == " ":
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
            return 'f'
        elif self.color=="black":
            return 'F'