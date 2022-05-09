from Chess_Game import pieces

class Pawn(pieces.Piece):

    def __init__(self,type,row,column,color):
        super().__init__(type, row, column,color) # super() charge les attribut de la classe mere
        self.first_move = True

    def get_available_moves(self,row,column,board): #connaitre le coup possible du pion
        self.clear_available_move()

        if self.color == "white":

            if row-1>=0: #verifie que l'on est pas au bord du plateau
                if board[row-1][column] == 0: #verifie qu'il n'y a pas de piece a la case inidquer
                    self.availables_moves.append((row - 1, column))
                    if self.first_move:
                        if board[row-2][column] == 0:
                            self.availables_moves.append((row - 2, column))

                if column-1 >=0:
                    if board[row-1][column-1] != 0:
                        piece = board[row-1][column-1]
                        if piece.color != self.color:
                            self.availables_moves.append((row - 1, column - 1))

                if column+1 >=len(board[0]):
                    if board[row - 1][column + 1] != 0:
                        piece = board[row-1][column+1]
                        if piece.color != self.color:
                            self.availables_moves.append((row - 1, column + 1))

        if self.color == "black":

            if row+1<len(board):

                if board[row+1][column] == 0:
                    self.availables_moves.append((row + 1, column))

                    if self.first_move:
                        if board[row+2][column] == 0:
                            self.availables_moves.append((row + 2, column))

                if column-1 >=0:
                    if board[row+1][column-1] != 0:
                        piece = board[row+1][column-1]
                        if piece.color != self.color:
                            self.availables_moves.append((row + 1, column - 1))

                if column+1 >=len(board[0]):
                    if board[row + 1][column + 1] != 0:
                        piece = board[row+1][column+1]
                        if piece.color != self.color:
                            self.availables_moves.append((row + 1, column + 1))

        return self.availables_moves

    def display(self):
        if self.color=="white":
            return "p"
        elif self.color=="black":
            return 'P'