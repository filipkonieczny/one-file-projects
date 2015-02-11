#!/usr/bin/env python
# encoding: utf-8


# this program creates porings, who travel on screen
# each poring, as he travels randomly, leaves trail
# when porings meet, one of them is destroyed
# therefore the name "last poring standing"


# imports
import pygame
from pygame import display
from pygame.locals import QUIT

import random


# classes
class Poring():
    '''Poring class - allows random movement
    '''

    def __init__(self, canvas, WIDTH, HEIGHT, x, y, w, h, color_rgb, previous_color):
        '''Constructor, takes poring's properties:

        (canvas, int, int, int, int, int, int, list)

        '''

        self.canvas = canvas
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_rgb = color_rgb
        self.previous_color = previous_color


    def move(self):
        '''Funtion guarantees "random" movement.
        It's also forbidden to go out of the board

        (int, int)

        '''

        # moving horizontally
        if self.x <= 0:
            self.x += random.randint(0, 1)

        elif self.x >= (self.WIDTH - 1):
            self.x += random.randint(-1, 0)

        else:
            self.x += random.randint(-1, 1)


        # moving vertically
        if self.y <= 0:
            self.y += random.randint(0, 1)

        elif self.y >= (self.HEIGHT - 1):
            self.y += random.randint(-1, 0)

        else:
            self.y += random.randint(-1, 1)


    def draw_white(self):
        '''Draws poring's previous position
        '''

        rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.canvas, self.previous_color, rect)


    def draw(self):
        '''Draws the poring on the canvas
        '''

        rect = (self.x, self.y, self.w, self.h)
        pygame.draw.rect(self.canvas, self.color_rgb, rect)


# variables
# screen size
WIDTH = 640
HEIGHT = 640

porings_count = 100
porings = []

move_count = 0


# main
# setup pygame
pygame.init()
canvas = display.set_mode((WIDTH, HEIGHT), 0, 16)
display.set_caption('PyGame - Last Poring Standing')


# create porings
for i in range(porings_count):
    porings.append(Poring(canvas, WIDTH, HEIGHT, random.randint(0, WIDTH), random.randint(0, HEIGHT), 2, 2, (255, 0, 0), (255, 255, 255)))

print len(porings)

canvas.fill((0, 0, 0))


# main loop
while True:
    # draw objects
    poring_positions = []

    for poring in porings:
        poring.draw_white()
        poring.move()
        poring.draw()

        # detect colision
        if (poring.x, poring.y) in poring_positions:
            porings.remove(poring)
            print("\t%d" % len(porings))

        else:
            poring_positions.append((poring.x, poring.y))


    # update display
    display.update()


    # print move count
    print(move_count)
    move_count += 1


    # if there's only 1 poring left, stop the game
    if len(porings) <= 1:
        break


    # handle window closing
    for event in pygame.event.get():
        if event.type is QUIT:
            pygame.quit()
            exit()
