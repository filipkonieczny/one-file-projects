#!/usr/bin/env python


# this program is a small representation of porings' random movement
 
 
# imports
import random
import time
 
 
# class declaration
class Poring():
    '''Poring class - allows random movement and id display.
   
   '''
   
    def __init__(self, position_x, position_y, id):
        '''Constructor, takes poring's position and id:
       
       (int, int, int)
       
       '''
       
        self.position_x = position_x
        self.position_y = position_y
        self.id = id
   
   
    def move(self, board_x_len, board_y_len):
        '''Funtion guarantees "random" movement.
       It's also forbidden to go out of the board
       
       (int, int)
       
       '''
       
        # moving horizontally
        if self.position_x <= 0:
            self.position_x += random.randint(0, 1)
       
        elif self.position_x >= (board_x_len - 1):
            self.position_x += random.randint(-1, 0)
       
        else:
            self.position_x += random.randint(-1, 1)
       
       
        # moving vertically
        if self.position_y <= 0:
            self.position_y += random.randint(0, 1)
       
        elif self.position_y >= (board_y_len - 1):
            self.position_y += random.randint(-1, 0)
       
        else:
            self.position_y += random.randint(-1, 1)
   
   
    def show_position(self):
        '''Informs about the Poring's position.
       
       -> string
       
       '''
       
        return (self.position_x, self.position_y)
 
 
    def show_id(self):
        '''Informs about the Poring's id.
       
       -> string
       
       '''
       
        return self.id
 
 
# function declaration
def ask_for_number(question, error_msg):
    '''Function asks for a number repeatedly if a number isn't given.
   
   (str, str) -> int
   
   >>> ask_for_number("Give a number: ", "Wrong.")
   Give a number: asdf
   Wrong.
   Give a number: 3
   3
   
   '''
   
    while True:
        user_input = raw_input(question)
       
        try:
            user_input = int(user_input)
       
        except ValueError:
            print(error_msg)
       
        else:
            return user_input
 
 
def number_in_range(number, n_min, n_max):
    '''Function checks if a given number is between specified ranges
   
   (int, int, int) ->
   
   >>> number_in_range(-1, 0, 100)
   False
   
   >>> number_in_range(1, 0, 100)
   True
   
   '''
   
    if number >= n_min and number <= n_max:
        return True
   
    else:
        return False
 
 
def ask_for_specific_number(question, error_msg, n_min, n_max):
    '''Function asks for a number between specific ranges.
   
   (str, str, int, int) -> int
   
   >>> ask_for_specific_number("Give x from 0 to 10", "Wrong", 0, 10)
   Give x from 0 to 10: a
   Wrong
   Give x from 0 to 10: 11
   Please keep the number between min and max.
   Give x from 0 to 10: 5
   5
   
   '''
   
    number = ask_for_number(question, error_msg)
   
    while not number_in_range(number, n_min, n_max):
        print("Please keep the number between min and max.")
       
        number = ask_for_number(question, error_msg)
       
    return number
 
 
def create_board(board_x, board_y, board):
    for row in range(0, board_y):
        board_row = []
       
        for column in range(0, board_x):
            board_row.append(".")
       
        board.append(board_row)
 
 
# main loop
print("Hello! This program simulates Porings' behaviour.")
print("Enjoy!\n\n")
 
 
while True:
    # variables declaration
    board = []
    porings = []
 
 
    # ask for the size of the board
    print("How big should the board be?(5x5 min, 20x20 max)")
   
    board_x = ask_for_specific_number("Board's length?(5-20): ", \
    "Wrong. Please give a number.\n", 5, 20)
   
    board_y = ask_for_specific_number("Board's height?(5-20): ", \
    "Wrong. Please give a number.\n", 5, 20)
   
   
    # create a board of desired size(board_y: rows, board_x: columns)
    create_board(board_x, board_y, board)
 
 
    # ask the user for the number of porings
    print("\nHow many porings would you like to see?(1-9)")
   
    porings_num = ask_for_specific_number("How many porings?(1-9): ",\
    "Wrong. Please give a number.\n", 1, 9)
   
   
    # creating porings
    porings_position = []
   
    for i in range(porings_num):
        porings.append(Poring(random.randint(0, board_x - 1), \
        random.randint(0, board_y - 1), (i + 1)))
        porings_position.append((porings[i].show_position()))
 
   
    # ask how many moves should be done
    print("\nHow many moves should every Poring do?(1-1000)")
   
    moves_num = ask_for_specific_number("How many moves?(1-1000): ", \
    "Wrong. Please give a number.\n", 1, 1000)
   
   
    # making moves
    for i in range(0, moves_num + 1):
        print("\nMove #%d:\n" % (i))
       
        # print the board
        while True:
            break
        for row in board:
            for i in row:
                print i,
               
            print("")
       
       
        # may not always for on every interpreter
        # play a sound every move
        #print("\a")
       
       
        # 1 sec delay
        #time.sleep(1)
       
       
        # clear the board
        #board = []
        #create_board(board_x, board_y, board)
       
       
        # move porings
        for i in porings:
            i.move(board_x, board_y)
           
            # make changes to the board
            board[i.position_y][i.position_x] = "P"
   
   
    # print porings' position changes
    print("\n\nThat's how the poring moved:")
   
    for i, item in enumerate(porings):
        print("#%d: Start position: (%d, %d), finish position: %s" %\
        (item.show_id(), \
        porings_position[i][0], \
        porings_position[i][1], \
        item.show_position()))
 
    # ask if user wants to repeat
    print("\nThat's about it.\n")
   
    repeat = ask_for_specific_number("Wanna repeat?(1/0): ", \
    "Wrong. Please give a number.\n", 0, 1)
   
    if repeat == 1:
        print("\nCool! Let's have some more fun!")
 
    else:
        print("\nThanks for playing, cheers!")
        break