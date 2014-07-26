#!/usr/bin/env python
# encoding: utf-8


# this program is a SLIDER game prototype
# a game in which there's a board and you get to slide rows and columns
# you do that to form combinations, for which you're getting points
# max board size should be no bigger than 6, max moves given in constant variables


# imports
import random


# constant variables
max_moves = 10
board_size = 3
rows = ("a", "b", "c", "d", "e", "f")
columns = ("1", "2", "3", "4", "5", "6")


# functions
def create_board(board, board_size, spots, rows):
    '''This function creates the board with randomly generated cubes.

    (dict, int, tuple)
    '''

    for i in range(board_size):
        board[rows[i]] = []
        for i2 in range(board_size):
            board[rows[i]].append(spots[random.randint(0, board_size - 1)])


def print_board(board, move_count):
    '''This function simply prints the board and number of moves.

    (dict, int)
    '''

    print("Move #%d:" % move_count)

    for key in sorted(board.keys()):
        for i in board[key]:
            print(i),
        
        print("")


def create_possible_moves(rows, columns, possible_moves, board_size):
    '''This function decides what are the possible moves.
    '''

    for row in rows:
        possible_moves.append("%s%s" % (row, "r"))
        possible_moves.append("%s%s" % (row, "l"))

    for column in columns:
        possible_moves.append("%s%s" % (column, "u"))
        possible_moves.append("%s%s" % (column, "d"))


def ask_to_move(move, question, possible_moves):
    '''This function asks the player to move.
    If it's not valid, asks again.

    (str, str, list)
    '''

    move = raw_input(question)

    while move not in possible_moves:
        print("Invalid input.")
        move = raw_input(question)

    return move


def move_horizontally(board_range, start_point, end_point, direction):
    '''This function moves the cubes horizontally.

    (int, int, int, int)
    '''

    for i in board_range:
        if i != start_point:
            if i == end_point:
                last_spot = board[move[0]][i]

            board[move[0]][i] = board[move[0]][i + direction]

        else:
            board[move[0]][i] = last_spot


def move_vertically(board_range, start_point, end_point, direction):
    '''This function moves the cubes vertically.

    (int, int, int, int)
    '''

    for i in board_range:
        if i != start_point:
            if i == end_point:
                last_spot = board[rows[i]][int(move[0]) - 1]

            board[rows[i]][int(move[0]) - 1] = board[rows[i + direction]][int(move[0]) - 1]

        else:
            board[rows[i]][int(move[0]) - 1] = last_spot


# variables
# a representation of colors in the game, max 6
spots = ("@", "#", "$", "%", "&", "+")
board = {}
possible_moves = []
move = ""
move_count = 0
score = 0


# main
# hello message
print("\nSLIDER\n")
print("A prototype of a game in which you get to:")
print("- slide rows and columns of cubes to form combinations,")
print("- you get points the bigger the combination,")
print("- once a combination is done it's replaced with new squares,")
print("- if you slide a row/column, a new cube replaces the previous one")
print("\nBoard: columns are numerical, rows alphabetical")
print("To move simply write row/column and direction, ex:")
print("br = move row b to the right, 3u = move column 3 up.")
print("\nEverything else is described in the documentation.\n\nEnjoy!\n\n")
print("Max moves: %d\n\n" % max_moves)


create_possible_moves(rows, columns, possible_moves, board_size)
create_board(board, board_size, spots, rows)


# main loop
while True:
    print_board(board, move_count)
    print("")

    if move_count == max_moves:
        break
    
    move = ask_to_move(move, "Where would you like to move?(ex: 1u, al): ", possible_moves)

    
    # move the cubes
    # rows
    if move[0] in rows:
        # right
        if move[1] == "r":
            move_horizontally(reversed(range(board_size)), 0, board_size - 1, -1)
        
        # left
        else:
            move_horizontally(range(board_size), board_size - 1, 0, 1)


    # columns
    else:
        # up
        if move[1] == "u":
            move_vertically(range(board_size), board_size - 1, 0, 1)


        # down
        else:
            move_vertically(reversed(range(board_size)), 0, board_size - 1, -1)


    # look for combinations for every cube
    comb_boards = {}

    for cube in range(board_size):
        comb_board = []
        # check every row
        for i, key in enumerate(sorted(board.keys())):
            # check every spot in the row
            for i2, spot in enumerate(board[key]):
                # if the spot matches the spot we are currently looking for
                if spot == spots[cube]:
                    comb_board.append("%s%d" % (sorted(board.keys())[i], i2))

                # print spot
                comb_boards[spots[cube]] = comb_board


    print comb_boards


    # rows
    if move[0] in rows:
        # for every spot in the row
        for i, spot in enumerate(board[move[0]]):
        # for i in range(board_size):
            # check if there are combinations horizontally
            # if ("%d%d" % (i, i2)) in comb_boards:
            #     pass
            if "%s%d" % (move[0], i) in comb_boards[spot]:
                # to the left
                if "%s%d" % (move[0], i - 1) in comb_boards[spot]:
                    board[move[0]][i] = "."
                    board[move[0]][i - 1] = "."

                # to the right
                # if "%s%d" % (move[0], i2 + 1) in comb_boards[spot]:
                #     board[move[0]][i2 - 1] = "."


    # columns
    else:
        # for every spot in the row
        for spot in comb_boards.keys():
            print spot
            for i in range(board_size):
                # pass
                # check if there are combinations horizontally
                # if ("%d%d" % (i, i2)) in comb_boards:
                #     pass
                # print sorted(board.keys())[i]
                # print board[sorted(board.keys())[i]]
                # print board[sorted(board.keys())[i]][int(move[0]) - 1]
                # print "%s%s" % (sorted(board.keys())[i], move[0])
                if "%s%s" % (sorted(board.keys())[i], move[0]) in comb_boards[spot]:
                    # up
                    print "%s%s" % (sorted(board.keys())[i - 1], move[0])
                    print "a"
                    if "%s%s" % (sorted(board.keys())[i - 1], move[0]) in comb_boards[spot]:
                        print "b"
                        print board[sorted(board.keys())[i]][int(move[0]) - 1]
                        board[sorted(board.keys())[i]][int(move[0]) - 1] = "."
                        board[sorted(board.keys())[i - 1]][int(move[0]) - 1] = "."


    # integrate all "." into the main board


    # replace "." with random spots
    # for row in board.keys():
    #     for i, spot in enumerate(board[row]):
    #         if spot == ".":
    #             board[row][i] = spots[random.randint(0, board_size - 1)]
    

    print("Score:", score)
    move_count += 1


# goodbye message
print("\n\nThanks for using me!!\n")