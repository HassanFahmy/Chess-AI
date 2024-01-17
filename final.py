import chess
import random

# white is true black is false

#weights go in order of peices so pawn is denoted by one and it has the first array
#it goes in order with knight then bishop, rook, queen, king each one has its own array
#each square on the biard is represented by an integer as it would appear in a rolled out array
#so the weights are rolled out arrays

weights = [
    [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 11.0, 11.0,
     12.0, 13.0, 13.0, 12.0, 11.0, 11.0, 10.5, 10.5, 11.0, 12.5, 12.5, 11.0, 10.5, 10.5, 10.0, 10.0, 10.0, 12.0, 12.0,
     10.0, 10.0, 10.0, 10.5, 9.5, 9.0, 10.0, 10.0, 9.0, 9.5, 10.5, 10.5, 11.0, 11.0, 8.0, 8.0, 11.0, 11.0, 10.5, 100.0,
     100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0],
    [23.0, 24.0, 25.0, 25.0, 25.0, 25.0, 24.0, 23.0, 24.0, 26.0, 28.0, 28.0, 28.0, 28.0, 26.0, 24.0, 25.0, 28.0, 29.0,
     29.5, 29.5, 29.0, 28.0, 25.0, 25.0, 28.5, 29.5, 30.0, 30.0, 29.5, 28.5, 25.0, 25.0, 28.0, 29.5, 30.0, 30.0, 29.5,
     28.0, 25.0, 25.0, 28.5, 29.0, 29.5, 29.5, 29.0, 28.5, 25.0, 24.0, 26.0, 28.0, 28.5, 28.5, 28.0, 26.0, 24.0, 23.0,
     24.0, 25.0, 25.0, 25.0, 25.0, 24.0, 23.0],
    [29.0, 30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 29.0, 30.0, 31.0, 31.0, 31.0, 31.0, 31.0, 31.0, 30.0, 30.0, 31.0, 31.5,
     32.0, 32.0, 31.5, 31.0, 30.0, 30.0, 31.5, 31.5, 32.0, 32.0, 31.5, 31.5, 30.0, 30.0, 31.0, 32.0, 32.0, 32.0, 32.0,
     31.0, 30.0, 30.0, 32.0, 32.0, 32.0, 32.0, 32.0, 32.0, 30.0, 30.0, 31.5, 31.0, 31.0, 31.0, 31.0, 31.5, 30.0, 29.0,
     30.0, 30.0, 30.0, 30.0, 30.0, 30.0, 29.0],
    [50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 50.5, 51.0, 51.0, 51.0, 51.0, 51.0, 51.0, 50.5, 49.5, 50.0, 50.0,
     50.0, 50.0, 50.0, 50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0,
     50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 49.5, 50.0, 50.0, 50.0, 50.0, 50.0, 50.0, 49.5, 50.0,
     50.0, 50.0, 50.5, 50.5, 50.0, 50.0, 50.0],
    [98.0, 99.0, 99.0, 99.5, 99.5, 99.0, 99.0, 98.0, 99.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 99.0, 99.0, 100.0,
     100.5, 100.5, 100.5, 100.5, 100.0, 99.0, 99.5, 100.0, 100.5, 100.5, 100.5, 100.5, 100.0, 99.5, 100.0, 100.0, 100.5,
     100.5, 100.5, 100.5, 100.0, 99.5, 99.0, 100.5, 100.5, 100.5, 100.5, 100.5, 100.0, 99.0, 99.0, 100.0, 100.5, 100.0,
     100.0, 100.0, 100.0, 99.0, 98.0, 99.0, 99.0, 99.5, 99.5, 99.0, 99.0, 98.0],
    [-3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0,
     -5.0, -5.0, -4.0, -4.0, -3.0, -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0, -2.0, -3.0, -3.0, -4.0, -4.0, -3.0,
     -3.0, -2.0, -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 3.0, 1.0,
     0.0, 0.0, 1.0, 3.0, 2.0]]


def evaluation_function(board, maxAgent):
    #because check mate is assigned weight infinity
    # the heristic does not really matter in the endgame
    #because this algorithm tapers off  it usually reaches that checkmate
    if board.is_checkmate():
        if board.turn is maxAgent:
            return -float('inf')
        elif board.turn is not maxAgent:
            return float('inf')
    elif board.is_stalemate() or board.is_insufficient_material():
        return 0
    else:
        evaluation = 0
        if board.turn is maxAgent:
            evaluation += board.legal_moves.count()/10
        else:
            evaluation -= board.legal_moves.count() / 10
        for i in range(64):
            piece_type = board.piece_type_at(i)
            if piece_type is not None:
                if board.color_at(i) is maxAgent:
                    evaluation += weights[piece_type - 1][-i - 1]
                else:
                    evaluation -= weights[piece_type - 1][i]

        return evaluation


def getAction(query_board, numturns, maxAgent, tapering_factor):

    #similar to branching factor tapering factor used by minmax to adjust factor it reduces depth by
    # when tapering factor is equal to branching factor the depth decreases by one for each turn
    #the higher the factor is the deeper the tree becomes

    numlayers = numturns

    def fminmax(numlayers, board, alpha, beta):
        if board.is_game_over() or numlayers <= 0:
            return tuple((evaluation_function(board, maxAgent), 0))

        if board.turn is maxAgent:
            value = (-float('inf'), 0)
            for move in board.legal_moves:
                boardcpy = board.copy()
                boardcpy.push(move)
                #if board.legal_moves.count() <= 5:
                #    value = max(value, (fminmax(numlayers - 0.25, boardcpy, alpha, beta)[0], move), key=lambda x: x[0])
                #else:
                value = max(value, (fminmax(numlayers -float(board.legal_moves.count()/tapering_factor), boardcpy, alpha, beta)[0], move), key=lambda x: x[0])
                alpha = max(value[0], alpha)
                # boardcpy.pop()
                if alpha >= beta:
                    break
            return value
        elif board.turn is not maxAgent:
            value = (float('inf'), 0)
            for move in board.legal_moves:
                boardcpy = board.copy()
                boardcpy.push(move)
                #if board.legal_moves.count() <= 5:
                 #   value = min(value, (fminmax(numlayers - 0.25, boardcpy, alpha, beta)[0], move), key=lambda x: x[0])
                #else:
                value = min(value, (fminmax(numlayers -float(board.legal_moves.count()/tapering_factor), boardcpy, alpha, beta)[0], move), key=lambda x: x[0])
                beta = min(value[0], beta)
                # boardcpy.pop()
                if alpha >= beta:
                    break
            return value



    return fminmax(numlayers, query_board, - float('inf'), float('inf'))[1]


main_board = chess.Board()
player = chess.WHITE
# capped it at 100 turns just in case something goes wrong, always wins before that though
for i in range(100):
    #could change this to while and comment out above loop when not testing
    if main_board.legal_moves:
        if  main_board.turn is not player:
            """move = 0
            while move not in main_board.legal_moves:
                #read move from user input 
             move = main_board.parse_san(input("your move"))
            main_board.push(move)"""
            # select random move to run fast when debugging
            main_board.push(random.choice(list(main_board.legal_moves)))
            # play against itself with different level
            # numturns = 3
            # main_board.push(getAction(main_board,numturns, player ))
        else:
            main_board.push(getAction(main_board, 4, player))
        print ("turn:", i)
        print (main_board)
