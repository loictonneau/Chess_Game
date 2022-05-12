from Chess_Game import bishop,king,knight,pawn,queen,rook

class Board:

    def __init__(self, row, columns):
        self.row = row
        self.columns = columns
        self.board = []
        self.create_board()

    def create_board(self):
        for column in range(self.columns):
            ligne=[]
            for row in range(self.row):
                ligne.append(" ")
            self.board.append(ligne)

        for row in range(self.row):
            for column in range(self.columns):
                if row == 1:
                    self.board[row][column] = pawn.Pawn("pawn", row, column, "black")
                if row == 6:
                    self.board[row][column] = pawn.Pawn("pawn", row, column, "white")
                if row == 0:
                    if column == 0 or column == 7:
                        self.board[row][column] = rook.Rook("rook", row, column, "black")
                    if column == 1 or column == 6:
                        self.board[row][column] = knight.Knight("knight", row, column, "black")
                    if column == 2 or column == 5:
                        self.board[row][column] = bishop.Bishop("bishop", row, column, "black")
                    if column == 3:
                        self.board[row][column] = queen.Queen("queen", row, column, "black")
                    if column == 4:
                        self.board[row][column] = king.King("king", row, column, "black")
                if row == 7:
                    if column == 0 or column == 7:
                        self.board[row][column] = rook.Rook("rook", row, column, "white")
                    if column == 1 or column == 6:
                        self.board[row][column] = knight.Knight("knight", row, column, "white")
                    if column == 2 or column == 5:
                        self.board[row][column] = bishop.Bishop("bishop", row, column, "white")
                    if column == 3:
                        self.board[row][column] = queen.Queen("queen", row, column, "white")
                    if column == 4:
                        self.board[row][column] = king.King("king", row, column, "white")

    def get_piece(self,row,column):
        return self.board[row][column]

    def move(self,piece,row,column):
        self.board[piece.row][piece.column],self.board[row][column] = self.board[row][column], self.board[piece.row][piece.column]
        if piece.type == "pawn":
            if piece.first_move:
                piece.first_move = False