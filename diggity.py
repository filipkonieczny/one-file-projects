#!/usr/bin/env python
# encoding: utf-8


# description
# diggity - a small mining game inspired by 'Dig To China' and #lowrezjam2014
# the goal is to dig as much score or as deep as you can
# there are a couple of types of blocks(basically rocks and gold)
# you've got 16 seconds of action(left bar), although time bonuses can be found
# only controls are left/right/down arrows and special skill at spacebar
# skill's charge is shown at the right bar
# made in around 7 hours of Blackstreet - Diggity (Bondax Edit), enjoy!


# imports
import pygame
from pygame import display
from pygame import key
from pygame.locals import QUIT

import random
import time
import math


# classes
class Player:
    '''
    Player class. Handles user input(moving, skills).

    __init__() - constructor, takes basic information about player
    _move() - internal function detecting collision and moving the player
    move() - upon receiving direction calls the right _move function
    skill() - activated when enough power is gathered and spacebar is get_pressed

    '''

    def __init__(self, x, y):
        '''
        Constructor.

        x, y - information about current position(x, y) on the board
        current_time - used to determine whether the user can move 

        '''

        self.current_time = 0
        self.x = x
        self.y = y


    def _move(self, board, x_dir, y_dir, hud):
        '''
        Internal function.
        Decides whether player can move and detects collisions.
        If a collision is detected calls a destroy function on the hit block.
        Clears the board after a move has been performed.

        '''

        # check what collisions
        # if a block hit
        if board[self.y + y_dir][self.x + x_dir].type != "nothing":
            # destroy the block
            board[self.y + y_dir][self.x + x_dir].destroy(hud)

        # if there's nothing in your way
        else:
            board[self.y][self.x].type = "nothing"
            board[self.y + y_dir][self.x + x_dir].type = "player"

            board[self.y + y_dir][self.x + x_dir]._update()

            # if we're moving horizontally
            if x_dir != 0:
                self.x += x_dir

            # if we're moving vertically
            else:
                sort_board(board, self.x, self.y)
                hud.depth += 1


    def move(self, board, direction, hud):
        '''
        This function decides what kind of move to perform based on direction.
        Upon deciding calls _move internal function.

        '''

        # if enough time has passed to perform a move
        if time.time() - self.current_time >= 0.5:
            self.current_time = time.time()

            # move left
            if direction == -1 and self.x != 0:
                self._move(board, -1, 0, hud)

            # move right
            elif direction == 1 and self.x != 32:
                self._move(board, 1, 0, hud)

            # move down
            else:
                self._move(board, 0, 1, hud)


    def skill(self, board, hud):
        '''
        Upon pressing spacebar special skill is activated.

        Special skill weakens everything on the current depth by 1 level.

        '''


        # weaken everything on the current self.y depth
        for i in board[self.y]:
            i.destroy(hud)

        # reset the power bar
        hud.power_factor = 0


class Block:
    '''
    Block class.
    It's a representation of any object displayed on the main screen.

    Enables drawing the block, destroying it and updating it's information.

    __init__ - constructor, assigns block type upon creating
    draw_block - simply draws the block on the screen
    _update - updates block's information like status and assigns colors
    destroy - lowers block's attributes, takes care of any corresponding action

    '''


    def __init__(self, block):
        '''
        Constructor.
        Upon creating a Block object it's type is evaluated and stored.

        block - when randomly generated it determines Block's type
        type - Block's type is stored here, it's also used in every method

        don't forget - if you want to add more types, add them in all methods

        '''

        self.block = block

        # time bonus
        if self.block == 2:
            block_type = "time bonus"

        # gold
        elif self.block >= 3 and self.block <= 5:
            block_type = "gold"

        # rock
        elif self.block >= 6 and self.block <= 13:
            block_type = "rock"

        # hard rock
        elif self.block >= 14 and self.block <= 21:
            block_type = "hard rock"

        # very hard rock
        elif self.block >= 22 and self.block <= 25:
            block_type = "very hard rock"

        # nothing
        elif self.block == 1:
            block_type = "nothing"

        # player
        else:
            block_type = "player"


        self.type = block_type

        self._update()


    def draw_block(self, x, y):
        '''
        This function draws the block based on it's type and position.

        (int, int) -> draw

        '''

        if self.type != "nothing":
            rect = (4 * SCALE + y * SCALE, x * SCALE, SCALE, SCALE)

            pygame.draw.rect(canvas, self.colors, rect)


    def _update(self):
        '''
        Updates information about the block itself based on current type.

        '''

        # time bonus
        if self.type == "time bonus":
            self.colors = (208, 70, 72)

        # gold
        elif self.type == "gold":
            self.colors = (218, 212, 94)

        # rock
        elif self.type == "rock":
            self.colors = (109, 194, 202)

        # hard rock
        elif self.type == "hard rock":
            self.colors = (89, 125, 206)

        # very hard rock
        elif self.type == "very hard rock":
            self.colors = (48, 52, 109)

        # nothing
        elif self.type == "nothing":
            self.colors = (222, 238, 214)

        # player
        else:
            self.colors = (109, 170, 44)


    def destroy(self, hud):
        '''
        'Destroys' the block, meaning it takes care of it's current state.
        Any occurence such as score increase, etc is taken care of here too.

        '''

        # time bonus
        if self.type == "time bonus":
            hud.time += 4
            hud.score += 1
            self.type = "nothing"

        # gold
        elif self.type == "gold":
            hud.score += 10
            self.type = "nothing"

        # rock
        elif self.type == "rock":
            hud.score += 1
            self.type = "nothing"

        # hard rock
        elif self.type == "hard rock":
            hud.score += 2
            self.type = "rock"

        # very hard rock
        elif self.type == "very hard rock":
            hud.score += 3
            self.type = "hard rock"


        # update block's state
        self._update()


class Hud:
    '''
    HUD class.
    All information are displayed here(time bar and power bar).

    __init__ - holds basic Hud attributes
    draw - draws the bars and takes care of the logic behind it

    '''

    def __init__(self):
        '''
        Constructor.

        time - time left for the player to interaction
        current_time - used for measuring seconds left
        power_factor, power - powerbar characteristics
        score, depth - statistics

        '''

        self.time = 16
        self.current_time = time.time()
        self.power_factor = 0
        self.power = 0
        self.score = 0
        self.depth = 0


    def draw(self):
        '''
        Draws the bars and handles their current state(time and power).

        '''

        # reset the value of time - maximum can be 16
        if self.time > 16:
            self.time = 16


        if time.time() - self.current_time >= 1:
            self.current_time = time.time()
            self.time -= 1

        # display time bar on the left side
        rect = (0, HEIGHT - self.time * 2 * SCALE, 4 * SCALE, 32 * SCALE)

        # if there's more than 5 seconds left display it normally
        if self.time > 5:
            alpha = 1

        # if there's <= 5 seconds left then start flashing
        else:
            sinx = math.sin(10 * time.time())
            alpha = (3 + sinx) / 4


        red_color = int(round(208 * alpha))
        colors = (red_color, 70, 72)

        pygame.draw.rect(canvas, colors, rect)


        # display power bar on the right side
        if self.power_factor < HEIGHT:
            self.power_factor += 0.5

        if self.power_factor % SCALE == 0:
            self.power = self.power_factor

        rect = (WIDTH - 4 * SCALE, HEIGHT - self.power, 4 * SCALE, 32 * SCALE)

        pygame.draw.rect(canvas, (210, 125, 44), rect)


# functions
def sort_board(board, player_x, player_y):
    '''
    This function sorts the board and adds another layer at the bottom.
    Simple as that.

    (2d list of integers, int, int)

    '''

    # sort all layers
    for i in range(31):
        board[i] = board[i + 1]

    # set the player at the proper position
    board[player_y][player_x].block = 0

    # clean the bottom
    board[31] = [1] * 24

    for i in range(24):
        board[31][i] = Block(random.randint(2, 25))


def main():
    '''
    Main function of the game.
    Takes care of everything: displaying content, user input, logic, etc.

    '''


    # declare variables
    time_at_start = time.time()
    current_time = time.time()
    score = 0
    depth = 0


    # setup the game
    # create the environment
    board = [2] * 32

    for i in range(32):
        board[i] = [2] * 24


    # fill the environment
    for i, row in enumerate(board):
        for i2 in range(len(board[i])):
            # randomly generated each block
            # more information about block types generation in Block class
            board[i][i2] = Block(random.randint(2, 25))


    # clean up the space at the beginning
    for i in range(2):
        for j in range(24):
            board[i][j] = Block(1)


    # place the player
    board[1][12] = Block(0)
    player = Player(12, 1)


    # create hud
    hud = Hud()


    # main loop
    while True:
        # fill the screen with background color
        canvas.fill((222, 238, 214))


        # draw left and right sidebars
        # left
        rect = (0, 0, 4 * SCALE, 32 * SCALE)
        pygame.draw.rect(canvas, (20, 18, 28), rect)

        # right
        rect = (WIDTH - (4 * SCALE), 0, 4 * SCALE, 32 * SCALE)
        pygame.draw.rect(canvas, (20, 18, 28), rect)


        # display hud
        if hud.time == 0:
            break

        hud.draw()


        # display content
        for i, row in enumerate(board):
            for j, block in enumerate(row):
                block.draw_block(i, j)


        # update display
        display.update()


        # handling events
        for event in pygame.event.get():
            # handling user input
            # left(user presses left arrow)
            if event.type == 2:
                # drilling(user presses space)
                if pygame.key.name(event.key) == "space":
                    if hud.power == HEIGHT:
                        player.skill(board, hud)

                # closing the program
                if  pygame.key.name(event.key) == "escape":
                    pygame.quit()
                    exit()

            # handling quit event
            if event.type is QUIT:
                pygame.quit()
                exit()


        # detecting player interaction
        keys = pygame.key.get_pressed()

        # if player presses left arrow
        if keys[pygame.K_LEFT]:
            player.move(board, -1, hud)

        # if player presses right arrow
        if keys[pygame.K_RIGHT]:
            player.move(board, 1, hud)

        # if player presses down arrow
        if keys[pygame.K_DOWN]:
            player.move(board, 0, hud)


    # display end game stats(time played, score, depth)
    print("\n\nYou've been playing for %.2f seconds." % (time.time() - time_at_start))
    print("Your score: %d." % hud.score)
    print("Your depth: %d." % hud.depth)
    print("\nThanks for playing!")


    # handling closing of the game after the user has lost
    while True:
        for event in pygame.event.get():
            # handling quit event on the screen
            if event.type is QUIT:
                pygame.quit()
                exit()

            # closing the program via keyboard
            if event.type == 2:
                if  pygame.key.name(event.key) == "escape":
                    pygame.quit()
                    exit()


# variables
# screen size
SCALE = 10
WIDTH = 32 * SCALE
HEIGHT = 32 * SCALE


# setup pygame
pygame.init()
canvas = display.set_mode((WIDTH, HEIGHT), 0, 16)
display.set_caption('diggity')


# run the main function
main()