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

    def select(self,row,column,selected=False):
        if self.selected:
            move = self._move(row,column)

            if not move:
                self.selected = None
                self.selected(row,column)
            piece = self.board.get_piece(row,column)
            if piece != 0 and self.turn == piece.color:
                self.selected = piece
                self.valid_moves = (row,column,self.board)

    def _move(self,row,column):
        piece = self.board.get_piece(row,column)
        if self.selected and (row,column) in self.valid_moves:
            if piece == 0 or piece != self.selected.color:
                if self.simulate_move(self.selected,row,column):
                    self.remove(self.selected,row,column)
                    self.board.move(piece,row,column)
                    self.change_turn()
                    self.valid_moves=[]
                    self.selected= None
                    return True
                return False
            return False

    def checkmate(self,board):
        king_pos = self.get_king_pos(board.Board)
        get_king = board.get_piece(king_pos[0],king_pos[1])
        king_available_moves =  set(get_king.get_availables_moves(king_pos[0], king_pos[1], board.Board))
        enemies_moves_set = set(self.enemies_moves(get_king, board.Board))
        king_moves = king_available_moves - enemies_moves_set
        set1 = king_available_moves.intersection(enemies_moves_set)
        possible_move_to_def = set1.intersection(self.possible_moves(board.Board))
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


    def simulate_move(self,piece,row,column):
        piece_row, piece_colomn = piece.row, piece.column
        save_piece = self.Board.Board[row][column]
        if self.Board.Board[row][column] != 0:
            self.Board.Board[row][column] = 0
        self.Board.Board[piece_row][piece_colomn],self.Board.Board[row][column] = self.Board.Board[row][column],self.Board.Board[piece_row][piece_colomn]
        king_pos = self.get_king_pos(self.Board.Board)
        if king_pos is self.enemies_moves(piece,self.Board.Board):
            piece.row,piece.column = piece_row,piece_colomn
            self.Board.Board[piece_row][piece_colomn] = piece
            self.Board.Board[row][column] = save_piece
            return False
        piece.row,piece_colomn = piece_row, piece_colomn
        self.Board.Board[piece_row][piece_colomn] = piece
        self.Board.Board[row][column] = save_piece
        return True

    def enemies_moves(self,piece,board):
        enemies_moves = []
        for row in range(len(board)):
            for column in range (len(board[row])):
                if board[row][column]!= 0 :
                    if board[row][column].color !=piece.color:
                        move = board[row][column].get_available_moves(row,column,board)
                        for moves in move:
                            enemies_moves.append(moves)
        return enemies_moves

    def get_king_pos(self,board):
        for row in range(len(board[0])):
            for column in range (len(board)):
                if board[row][column] != 0:
                    if board[row][column].type == "king" and board[row][column].color == self.turn:
                        return(row,column)


    def possible_moves(self, board):
        possible_move=[]
        for row in range(len(board.Board[0])):
            for column in range(len(board.Board)):
                if board[row][column] != 0:
                    if board[row][column].color == self.turn and board[row][column].type != "king":
                        moves = board[row][column].get_availabes_moves(row,column,board)
                        for move in moves:
                            possible_move.append(move)
            return possible_move


    def remove(self,board,piece,row,column):
        if piece !=0:
            board[row][column] = 0
            if piece.color == "white":
                self.white_pieces_left -=1
            else:
                self.black_pieces_left-=1

    def draw_available_move(self):
        if len(self.valid_moves) > 0:
            for pos in self.valid_moves:
                self.board[self.row][self.column] == 0
                self.board.draw_board()