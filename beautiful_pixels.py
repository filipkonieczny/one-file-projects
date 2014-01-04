#!/usr/bin/env python
# encoding: utf-8


# this program displays 16 squares showing off colors selected by DawnBringer
# a color palette made of 16 colors, as found here:
# http://www.pixeljoint.com/forum/forum_posts.asp?TID=12795
# discovered while checking out Clint Bellanger's Heroine Dusk.


# imports
import pygame
from pygame import display
from pygame.locals import QUIT


# variables
# screen size
WIDTH = 480
HEIGHT = 480
x = 0
y = 0

pixels = (
	(20, 12, 28),
	(68, 36, 52),
	(48, 52, 109),
	(78, 74, 78),
	(133, 76, 48),
	(52, 101, 36),
	(208, 70, 72),
	(117, 113, 97),
	(89, 125, 206),
	(210, 125, 44),
	(133, 149, 161),
	(109, 170, 44),
	(210, 170, 153),
	(109, 194, 202),
	(218, 212, 94),
	(222, 238, 214)
)

pixels_data = {}

# main
# setup pygame
pygame.init()
canvas = display.set_mode((WIDTH, HEIGHT), 0, 16)
display.set_caption('Beautiful Pixels')


canvas.fill((0, 0, 0))

# printing all pixels
for i in pixels:
	print x, y, i

	rect = (120 * x, 120 * y, 120, 120)
	pygame.draw.rect(canvas, i, rect)

	i = str(i)

	pixels_data[(x, y)] = i


	if x < 3:
		x += 1

	else:
		x = 0
		y += 1


# update display
display.update()


# main loop
while True:
    # handle events
    for event in pygame.event.get():
    	# handle mouse click detection
    	if event.type == pygame.MOUSEBUTTONUP:
    		pos = pygame.mouse.get_pos()
    		print("The color you're looking for is: %s, row %d, column %d" % (pixels_data[(pos[0] / 120, pos[1] / 120)], pos[1] / 120 + 1, pos[0] / 120 + 1))


    	# handle window closing
        if event.type is QUIT:
            pygame.quit()
            exit()