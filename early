import chess
import random

#white is true black is false

weights =[[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 11.0, 11.0, 12.0, 13.0, 13.0, 12.0, 11.0, 11.0, 10.5, 10.5, 11.0, 12.5, 12.5, 11.0, 10.5, 10.5, 10.0, 10.0, 10.0, 12.0, 12.0, 10.0, 10.0, 10.0, 10.5, 9.5, 9.0, 10.0, 10.0, 9.0, 9.5, 10.5, 10.5, 11.0, 11.0, 8.0, 8.0, 11.0, 11.0, 10.5, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],[23.0, 24.0, 25.0, 25.0, 25.0, 25.0, 24.0, 23.0, 24.0, 26.0, 28.0, 28.0, 28.0, 28.0, 26.0, 24.0, 25.0, 28.0, 29.0, 29.5, 29.5, 29.0, 28.0, 25.0, 25.0, 28.5, 29.5, 30.0, 30.0, 29.5, 28.5, 25.0, 25.0, 28.0, 29.5, 30.0, 30.0, 29.5, 28.0, 25.0, 25.0, 28.5, 29.0, 29.5, 29.5, 29.0, 28.5, 25.0, 24.0, 26.0, 28.0, 28.5, 28.5, 28.0, 26.0, 24.0, 23.0, 24.0, 25.0, 25.0, 25.0, 25.0, 24.0, 23.0],[29.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 29.0, 30.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 30.0, 30.0, 31.0, 31.5, 32.0, 32.0, 31.5, 31.0, 30.0, 30.0, 31.5, 31.5, 32.0, 32.0, 31.5, 31.5, 30.0, 30.0, 31.0, 32.0, 32.0, 32.0, 32.0, 31.0, 30.0, 30.0, 32.0, 32.0, 32.0, 32.0, 32.0, 32.0, 30.0, 30.0, 31.5, 31.0, 31.0, 31.0, 31.0, 31.5, 30.0, 29.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 29.0],[50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.5, 51.0, 51.0, 51.0, 51.0, 51.0, 51.0, 50.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 50.0, 50.0, 50.0, 50.5, 50.5, 50.0, 50.0, 50.0], [98.0, 99.0, 99.0, 99.5, 99.5, 99.0, 99.0, 98.0, 99.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 99.0, 99.0, 100.0, 100.5, 100.5, 100.5, 100.5, 100.0, 99.0, 99.5, 100.0, 100.5, 100.5, 100.5, 100.5, 100.0, 99.5, 100.0, 100.0, 100.5, 100.5, 100.5, 100.5, 100.0, 99.5, 99.0, 100.5, 100.5, 100.5, 100.5, 100.5, 100.0, 99.0, 99.0, 100.0, 100.5, 100.0, 100.0, 100.0, 100.0, 99.0, 98.0, 99.0, 99.0, 99.5, 99.5, 99.0, 99.0, 98.0],  [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,     -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0,     -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0,     -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0,     2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ,     2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ] ]
def evaluation_function (board):
    if board.is_checkmate():
        if board.turn:
            return -float('inf')
        elif not board.turn:
            return float('inf')
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0
    else:
        evaluation = 0
        for i in range (64):
            piece_type = board.piece_type_at(i)
            if piece_type is not None:
                if board.color_at(i):
                    evaluation += weights[piece_type-1][-i-1]
                else:
                    evaluation -= weights[piece_type-1][i]
        return evaluation


def getAction(query_board):

    def fminmax(numlayers, board, alpha, beta):
        if board.is_game_over() or numlayers <= 0:
            return tuple((evaluation_function(board),0))
        if board.turn:
            value = (-float('inf'), 0)
            sorted_moves = []
            for move in board.legal_moves:
                boardcpy = board.copy()
                boardcpy.push(move)
                sorted_moves.append((evaluation_function(boardcpy),boardcpy))
            sorted_moves.sort(key = lambda x: x[0] , reverse = True)

            for heuristic, boardcpy in sorted_moves:
                if board.legal_moves.count() <= 1:
                    value = max (value, (fminmax(numlayers-0.25, boardcpy, alpha, beta)[0], move),  key = lambda x: x[0])
                else:
                    value = max(value, (fminmax(numlayers-1, boardcpy, alpha, beta)[0], move), key=lambda x: x[0])
                alpha = max (value[0], alpha)
                #boardcpy.pop()
                if alpha >= beta:
                    break
            return  value
        elif not board.turn:
            value = (float('inf'), 0)
            sorted_moves = []
            for move in board.legal_moves:
                boardcpy = board.copy()
                boardcpy.push(move)
                sorted_moves.append((evaluation_function(boardcpy), boardcpy))
            sorted_moves.sort(key=lambda x: x[0], reverse=True)

            for heuristic, boardcpy in sorted_moves:
                if board.legal_moves.count() <=1:
                    value = min(value, (fminmax(numlayers -0.25, boardcpy, alpha, beta)[0], move), key=lambda x: x[0])
                else:
                    value = min(value, (fminmax(numlayers-1, boardcpy, alpha, beta)[0] , move), key=lambda x: x[0])
                beta = min(value[0], beta)
                #boardcpy.pop()
                if alpha >= beta:
                    break
            return value


    numlayers = 4
    return fminmax(numlayers, query_board, - float('inf') ,float('inf') )[1]


main_board = chess.Board()
for i in range (80):
    if not main_board.turn:
        """move = 0
        while move not in main_board.legal_moves:
            move = main_board.parse_san(input("your move"))
        main_board.push(move)"""
        main_board.push(random.choice(list(main_board.legal_moves)))
    else:
        main_board.push(getAction(main_board))
    print ("turn:", i)
    print (main_board)
