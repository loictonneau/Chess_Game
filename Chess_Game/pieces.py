class Piece:
    def __init__(self, type, row, column, color):
        self.type = type
        self.row = row
        self.column = column
        self.color = color
        self.availables_moves=[]


    def clear_available_move(self):
        if len(self.availables_moves) > 0:
            self.availables_moves = []

    def piece_move(self, row, column):
        self.row = row
        self.column = column