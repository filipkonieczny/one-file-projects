#!/usr/bin/env python


# tic-tac-toe!
 
 
# functions declarations
def print_board(rows, move_count):
    '''This function prints the board and current move number.
   
   (dict, int) -> print board layout
   
   '''
   
    print("\n 1 2 3")
   
    for row in sorted(rows.keys()):
        print row,
       
        for spot in rows[row]:
            print spot,
       
        print("")
 
 
def move(rows, available_moves, move_count):
    '''This function is used for adding a move to the board.
   
   (dict, list, int) -> (dict, list, int, int)
   
   '''
 
    print("\nMove #%i:"% move_count)
 
    move_count += 1
   
    if move_count % 2 == 0:
        player = "O"
   
    else:
        player = "X"
   
   
    move_input_text = "Player '%s' to move: " % player
    move_input = raw_input(move_input_text)
   
    while True:        
        if move_input not in available_moves:
            move_input = raw_input(move_input_text) # error msg?
       
        else:
            for i, item in enumerate(available_moves):
                if item == move_input:
                    available_moves.pop(i)
           
            break
       
   
    rows[move_input[0]][int(move_input[1]) - 1] = player
   
 
    return(rows, available_moves, player, move_count)
 
 
def win_condition(rows):
    '''This function is used to decide whether a game's been won.
   (dict) -> int
   
   '''
   
    # check for a win condition in rows
    for row in rows.keys():
        if rows[row][0] == rows[row][1] and \
        rows[row][1] == rows[row][2] and \
        rows[row][2] != ".":
            return 1
   
   
    # check for a win condition in columns
    for column in (0, 1, 2):
        if rows["A"][column] == rows["B"][column] and \
        rows["B"][column] == rows["C"][column] and \
        rows["C"][column] != ".":
            return 1
   
   
    # check for 2 diagonal win conditions
    if rows["A"][0] == rows["B"][1] and \
    rows["B"][1] == rows["C"][2] and \
    rows["C"][2] != ".":
        return 1
   
   
    if rows["A"][2] == rows["B"][1] and \
    rows["B"][1] == rows["C"][0] and \
    rows["C"][0] != ".":
        return 1
   
   
    # if win condition not found
    return 0
 
 
# variables declaration
rows = {
    "A": [
        ".",
        ".",
        "."
    ],
    "B": [
        ".",
        ".",
        "."
    ],
    "C": [
        ".",
        ".",
        "."
    ]
}
 
available_moves = [
    "A1",
    "A2",
    "A3",
    "B1",
    "B2",
    "B3",
    "C1",
    "C2",
    "C3"
]
 
 
move_count = 1
 
 
# main loop
print("Hello! Wanna play some tic-tac-toe?\n")
 
while True:
    print_board(rows, move_count)
   
    result = win_condition(rows)
   
    if move_count == 10 or result == 1:
        break
   
    else:
        move_result = move(rows, available_moves, move_count)
        move_count = move_result[-1]
 
 
# win condition satisfied or not
if result == 1:
    print("\n\nPlayer '%s' won!" % move_result[-2])
 
else:
    print("\n\nIt's a tie!")
 
 
print("\nThanks for playing!")