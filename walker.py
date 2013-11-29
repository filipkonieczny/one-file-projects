#!/usr/bin/env python

# this program creates a small board, randomly places a player and enables movement

# imports
import random


# variables
board = []
move_count = 0
commands = ["N", "S", "W", "E", "0"]

# main
# hello message
print("\nHello! This program let's you fool around a bit!")
print("Creates a board of a given size and allows you to move.")
print("\nEnjoy!\n\n")


# create the board
board_size = 10

for i in range(board_size):
	row = []

	for i2 in range(board_size):
		row.append(".")

	board.append(row)


# randomly place a player on the board
board[random.randint(0, board_size - 1)][random.randint(0, board_size - 1)] = "P"

# main loop
while True:
	# print the board
	print("Move #%i:" % move_count)

	for row in board:
		for i in row:
			print i,

		print("")

	print("")


	# find the player on the board
	position = []

	for i in range(board_size):
		for i2, spot in enumerate(board[i]):
			if spot == "P":
				position = [int(i), int(i2)]

				break


	# take commands from the user
	command_text = "Where would you like to move?(N/S/W/E, 0 to quit): "
	command = raw_input(command_text)

	command = command.upper()

	while command not in commands:
		print("\nError. Wrong input.")

		command = raw_input(command_text)

		command = command.upper()


	# move the player on the board
	# up
	if command == "N":
		if position[0] != 0:
			board[position[0]][position[1]] = "."

			position[0] -= 1

			board[position[0]][position[1]] = "P"

	# down
	elif command == "S":
		if position[0] + 1 != board_size:
			board[position[0]][position[1]] = "."

			position[0] += 1

			board[position[0]][position[1]] = "P"

	# left
	elif command == "W":
		if position[1] != 0:
			board[position[0]][position[1]] = "."

			position[1] -= 1

			board[position[0]][position[1]] = "P"

	# right
	elif command == "E":
		if position[1] + 1 != board_size:
			board[position[0]][position[1]] = "."

			position[1] += 1

			board[position[0]][position[1]] = "P"

	# quit(command == "0")
	else:
		break


	print("\n")


	# increase move_count
	move_count += 1


# goodbye message
print("\n\nThanks for using me!!\n")