from Chess_Game import constents
from Chess_Game import game



def get_postion(choice):
    letter = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
    choice_piece_list = list(choice)
    choice_piece_list[0] = letter.get(choice_piece_list[0])
    choice_piece_list[1] = int(choice_piece_list[1]) - 1
    return choice_piece_list

def main():
    playing_board = game.Game(constents.height,constents.witdh)
    playing_board.draw_board()
    choice_piece = "g1"  # input("selectioné une pièce")
    choice_piece_ = get_postion(choice_piece)
    game.Game.select(playing_board,choice_piece_[0],choice_piece_[1])
    choice_move = "f1"  # input("selectionné sa destination")
    choice_move_ = get_postion(choice_move)
    game.Game.select(playing_board, choice_move_[0], choice_move_[1])
    playing_board.draw_board()




main()