from Chess_Game import board

class Game:

    def __init__(self,rows,columns):
        self.board = board.Board(rows, columns)
        self.selected=None
        self.turn = "white"
        self.valid_moves = []
        self.black_pieces_left = 16
        self.white_pieces_left = 16

    def draw_board(self) :
        letters = ("A","B","C","D","E","F","G","H")
        print("  [ 1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ]")
        for row in range(self.board.row):
           print(letters[row],self.board.board[row])

    def reset(self,rows,columns):
        self.board = board.Board(rows, columns)
        self.selected = None
        self.turn = "white"
        self.valid_moves = []
        self.black_pieces_left = 16
        self.white_pieces_left = 16

    def change_turn(self):
        if self.turn == "white":
            self.turn = "black"
        else :
            self.turn = "white"

    def select(self,row,column):
        if self.selected:
            move = self._move(row, column)
            if not move:
                self.selected = None
                self.select(row, column)
        else :
            piece = self.board.get_piece(row, column)
            if piece == " " :
                return print("pas de piece a l'endroit choisie")
            elif self.turn != piece.color:
                    return print("cette piece ne vous appartient pas")
            else:
                self.selected = piece
                self.valid_moves = piece.get_available_moves(row,column,self.board.board)
                print(self.valid_moves)
                return piece


    def _move(self,row,column):
        piece = self.board.get_piece(row, column)
        if self.selected and (row,column) in self.valid_moves:
            if piece == " " or piece != self.selected.color:
                if self.simulate_move(self.selected,row,column):
                    self.board.move(self.selected,row,column)
                    self.remove(self.board.board,piece,row,column)
                    self.change_turn()
                    self.valid_moves=[]
                    self.selected= None
                    return True
                return False
            return False


    def checkmate(self,board):
        king_pos = self.get_king_pos(board.board)
        get_king = board.get_piece(king_pos[0],king_pos[1])
        king_available_moves = set(get_king.get_available_moves(king_pos[0],king_pos[1],self.board.board))
        enemies_moves_set = set(self.enemies_moves(get_king, board.board))
        king_moves = king_available_moves - enemies_moves_set
        set1 = king_available_moves.intersection(enemies_moves_set)
        possible_move_to_def = set1.intersection(self.possible_moves(board.board))
        if len(king_moves) == 0 and len(king_available_moves) !=0 and possible_move_to_def == 0:
            return True
        return False

    def check_game(self):
        if self.checkmate(self.board):
            if self.turn == "white":
                print("Black wins")
                return True
            else :
                print("White wins")
                return True

    def simulate_move(self, piece, row, column):
        piece_row, piece_colomn = piece.row, piece.column
        save_piece = self.board.board[row][column]
        if self.board.board[row][column] != " ":
            self.board.board[row][column] = " "
        self.board.board[piece_row][piece_colomn], self.board.board[row][column] = self.board.board[row][column], self.board.board[piece_row][piece_colomn]
        king_pos = self.get_king_pos(self.board.board)
        if king_pos is self.enemies_moves(piece, self.board.board):
            piece.row, piece.column = piece_row, piece_colomn
            self.board.board[piece_row][piece_colomn] = piece
            self.board.board[row][column] = save_piece
            return False
        piece.row, piece_colomn = piece_row, piece_colomn
        self.board.board[piece_row][piece_colomn] = piece
        self.board.board[row][column] = save_piece
        return True

    def enemies_moves(self,piece,board):
        enemies_moves = []
        for row in range(len(board)):
            for column in range (len(board[row])):
                if board[row][column]!= " " :
                    if board[row][column].color !=piece.color:
                        move = board[row][column].get_available_moves(row,column,board)
                        for moves in move:
                            enemies_moves.append(moves)
        return enemies_moves

    def get_king_pos(self,board):
        for row in range(len(board[0])):
            for column in range (len(board)):
                if board[row][column] != " ":
                    if self.board.board[row][column].type == "king" and board[row][column].color == self.turn:
                        return(row,column)


    def possible_moves(self, board):
        possible_move=[]
        for row in range(len(self.board.board[0])):
            for column in range(len(self.board.board)):
                if board[row][column] != " ":
                    if board[row][column].color == self.turn and board[row][column].type != "king":
                        moves = self.board.board[row][column].get_available_moves(row,column,board)
                        for move in moves:
                            possible_move.append(move)
            return possible_move


    def remove(self,board,piece,row,column):
        if piece !=" ":
            board[row][column] = " "
            if piece.color == "white":
                self.white_pieces_left -=1
            else:
                self.black_pieces_left-=1
