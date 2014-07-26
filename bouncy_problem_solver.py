#!/usr/bin/env python
import random
import time

# documentation at line 104, because I explain everything to the user anyway
# probably not the smartest move, but well... YOLO


# functions
def print_board(board):
	'''
	Function takes a board and prints it.

	(list) -> print

	>>> board = [["#", "#", "."], ["#", "#", "#"]]
	>>> print_board(board, 2)
	  0 1 2
	0 # # .
	1 # # #

	'''

	print(" "),

	len_row = 0

	for row in board:
		if len(row) >= len_row:
			len_row = len(row)

	for i in range(len_row):
		print(i),

	print("")

	for i, layer in enumerate(board):
		print(i),

		for item in layer:
			print(item),

		print("")


def add_connection(dot_search, dots_pos, connections):
	'''
	Adds a connection if one is possible. Prevents a duplication of connections.

	(string, list, list) -> list
	'''

	if dot_search in dots_pos:
		connection = ["%s%s" % (dot, dot_search), "%s%s" % (dot_search, dot)]
			
		if len(connections) != 0:
			for i in connections:
				if i == connection or [i[-1], i[0]] == connection:
					same_connections = 1
					break

				else:
					same_connections = 0

			
			if same_connections == 0:
				connections.append(connection)

		else:
			connections.append(connection)

	return(connections)


# variables
accuracy = 100
max_connections = 0
connections = []
paths = {}
board_display = []
time_at_start = time.time()

# creating a board
board = []
board_layer = []

# first coordinate is row, second is column, eg. "13" means row 1, column 3
dots_pos = []


# taking a problem(max size 9x9, honestly bigger than 6x6 make no sense)
# "#" are the dots, it's just easier to visualize the problem
problem = ''' ##
####
####
 ##'''


# main
# hello message
print("\nThis program solves any given problem under conditions of BOUNCY.")
print("BOUNCY being based on paper soccer game, has similiar rules.")
print("The goal is simple: make the most connections.")
print("No win/lose condition. Just make the most connections between the dots.")
print("It takes a problem, finds various connections paths and prints them.")
print("The path with the most connections is printed step by step.\n")
print("Accuracy of this search may vary, depending on the size of the problem.")
print("Bigger(3x3+) problems may require more insight.")
print("To change accuracy, set to 100 by default, go to line 76.")
print("\nEnjoy!\n\n")

# creates the board of the problem
for i, item in enumerate(problem):
	if item != "\n":
		board_layer.append(item)
		
	else:
		board.append(board_layer)
		board_layer = []


# problem is printed, unsolved
print("First coordinate - row, second - column.\n")
print_board(board)


# scan position of every dot(which are starting positions as well)
for i, layer in enumerate(board):
	for i2, item in enumerate(layer):
		if item == "#":
			position = "%d%d" % (i, i2)
			dots_pos.append(position)


# determine maximum number of connections
# check for possible connections
# every variation for every dot is now created in the "yxYX, YXyx" format
for dot in dots_pos:
	# upper left
	if dot[0] != 0 and dot[1] != 0:
		dot_search = "%d%d" % (int(dot[0]) - 1, int(dot[1]) - 1)

		add_connection(dot_search, dots_pos, connections)

	# up
	if dot[0] != 0:
		dot_search = "%d%d" % (int(dot[0]) - 1, int(dot[1]))

		add_connection(dot_search, dots_pos, connections)

	# upper right
	if dot[0] != 0 and dot[1] != len(board[0]):
		dot_search = "%d%d" % (int(dot[0]) - 1, int(dot[1]) + 1)

		add_connection(dot_search, dots_pos, connections)

	# right
	if dot[1] != len(board[int(dot[0])]):
		dot_search = "%d%d" % (int(dot[0]), int(dot[1]) + 1)

		add_connection(dot_search, dots_pos, connections)

	# lower right
	if dot[0] != len(board) and dot[1] != len(board[int(dot[0])]):
		dot_search = "%d%d" % (int(dot[0]) + 1, int(dot[1]) + 1)

		add_connection(dot_search, dots_pos, connections)

	# low
	if dot[0] != len(board):
		dot_search = "%d%d" % (int(dot[0]) + 1, int(dot[1]))

		add_connection(dot_search, dots_pos, connections)

	# lower left
	if dot[0] != len(board) and dot[1] != 0:
		dot_search = "%d%d" % (int(dot[0]) + 1, int(dot[1]) - 1)

		add_connection(dot_search, dots_pos, connections)

	# left
	if dot[1] != 0:
		dot_search = "%d%d" % (int(dot[0]), int(dot[1]) - 1)

		add_connection(dot_search, dots_pos, connections)


max_connections = len(connections)

# print number of connections(max)
print "\nMaximum number of connections possible:", max_connections

# for every starting point
for starting_pos in dots_pos:
	foo = 0

	# while loop created for accuracy
	while True:
		# create a clean possible_connections and available_connections list
		possible_connections = []
		available_connections = []

		for connection in connections:
			possible_connections.append(connection)


		# creating a path and copy starting position into pos variable
		path = []
		pos = starting_pos


		while True:
			# find out which connections are available out of possible connections
			for connection in possible_connections:
				if connection[0][0:2] == pos:
					available_connections.append(connection[0])

				elif connection[0][2:] == pos:
					available_connections.append(connection[1])

			# stop the program if there are no available connections(player stuck)
			if len(available_connections) == 0:
				break

			# randomly choosing a direction
			path_direction = available_connections[random.randint(0, len(available_connections) - 1)]
			available_connections.remove(path_direction)
			path.append(path_direction)


			# remove this direction from possible_connections
			for connection in possible_connections:
				if connection[0] == path_direction or connection[1] == path_direction:
					possible_connections.remove(connection)


			# change position
			pos = path_direction[2:]

			# clear available_connections
			available_connections = []


			# finish if there are no possible connections left
			if len(possible_connections) == 0:
				break


		paths[len(path)] = path

		foo += 1

		# accuracy
<<<<<<< HEAD
		if foo >= 10000:
=======
		if foo >= accuracy * max_connections:
>>>>>>> c44273946d58f5972bea32299b2313fe95e98768
			break


# printing all paths
for path in paths.keys():
	# print "Connections: %d, path: %s" % (path, paths[path])
	print "Connections: %d, path:" % path,

	for i in paths[path]:
		print i,

	print("")


# printing every move for the longest connection
# find width of the rows
row_width = 0

for row in board:
	for i in row:
		if len(row) >= row_width:
			row_width = len(row)

# creating a display board
for row in board:
	layer = []

	for i in row:
		layer.append(i)
		layer.append(" ")

	board_display.append(layer)

	layer = []
	for i in range(row_width):
		layer.append(" ")
		layer.append(" ")

	board_display.append(layer)


# selecting the longest connection
longest_connection = sorted(paths.keys())[-1]


# displaying every move
print("\n\nStep by step for the longest connection:\n")

foo = 0

while foo < int(longest_connection):
	print "#%i: %s" % (foo + 1, paths[longest_connection][foo])

	current_direction = paths[longest_connection][foo]

	# horizontally
	if current_direction[0] == current_direction[2]:
		# left
		if int(current_direction[1]) > int(current_direction[3]):
			board_display[int(current_direction[0]) * 2][(int(current_direction[1]) * 2) - 1] = "-"

		# right
		else:
			board_display[int(current_direction[0]) * 2][(int(current_direction[3]) * 2) - 1] = "-"

	# vertically
	elif current_direction[1] == current_direction[3]:
		# up
		if int(current_direction[0]) > int(current_direction[2]):
			board_display[(int(current_direction[0]) * 2) - 1][int(current_direction[1]) * 2] = "|"

		# down
		else:
			board_display[(int(current_direction[2]) * 2) - 1][int(current_direction[1]) * 2] = "|"

	# diagonally
	else:
		# up right
		if current_direction[0] > current_direction[2] and current_direction[1] < current_direction[3]:
			if board_display[(int(current_direction[0]) * 2) - 1][(int(current_direction[3]) * 2) - 1] != " ":
				board_display[(int(current_direction[0]) * 2) - 1][(int(current_direction[3]) * 2) - 1] = "X"

			else:
				board_display[(int(current_direction[0]) * 2) - 1][(int(current_direction[3]) * 2) - 1] = "/"

		# up left
		elif current_direction[0] > current_direction[2] and current_direction[1] > current_direction[3]:
			if board_display[(int(current_direction[0]) * 2) - 1][(int(current_direction[1]) * 2) - 1] != " ":
				board_display[(int(current_direction[0]) * 2) - 1][(int(current_direction[1]) * 2) - 1] = "X"

			else:
				board_display[(int(current_direction[0]) * 2) - 1][(int(current_direction[1]) * 2) - 1] = "\\"

		# down right
		elif current_direction[0] < current_direction[2] and current_direction[1] < current_direction[3]:
			if board_display[(int(current_direction[2]) * 2) - 1][(int(current_direction[3]) * 2) - 1] != " ":
				board_display[(int(current_direction[2]) * 2) - 1][(int(current_direction[3]) * 2) - 1] = "X"

			else:
				board_display[(int(current_direction[2]) * 2) - 1][(int(current_direction[3]) * 2) - 1] = "\\"

		# down left
		else:
			if board_display[(int(current_direction[2]) * 2) - 1][(int(current_direction[1]) * 2) - 1] != " ":
				board_display[(int(current_direction[2]) * 2) - 1][(int(current_direction[1]) * 2) - 1] = "X"

			else:
				board_display[(int(current_direction[2]) * 2) - 1][(int(current_direction[1]) * 2) - 1] = "/"


	# displaying every move
	for row in board_display:
		for i in row:
			print i,

		print ("")

	print("")

	foo += 1

# goodbye message
print("\nCalculated in %.2f seconds!" % (time.time() - time_at_start))
print("Thanks for using me!\n\n")