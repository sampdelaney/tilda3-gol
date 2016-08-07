### Author: Sam Delaney
### Description: Game of Life (Press A to reset)
### Category: Games
### License: MIT
### Appname: GoL
### Built-in: no

import pyb
import math
import ugfx
import buttons
import array
import os

ugfx.init()
buttons.init()
 
def game_of_life():
	width = 32
	height = 32
	cell_width = 8
	cell_height = 8
	grid = [[0 for x in range(width)] for y in range(height)]
	
	def seed():
		for x in range(1, width):
			for y in range(1, height):
				if pyb.rng() % 2 == 1:
					grid[x][y] = 1
				else:
					grid[x][y] = 0
	
	def display():
		for x in range(1, width):
			for y in range(1, height):
				if grid[x][y] == 1:
					ugfx.area((x-1)*cell_width+1,(y-1)*cell_height, cell_width, cell_height, ugfx.BLACK)
				else:
					ugfx.area((x-1)*cell_width+1,(y-1)*cell_height, cell_width, cell_height, ugfx.WHITE)
		
	def step():
		changed = 0
		for x in range(1, width):
			for y in range(1, height):
				n = 0
				# 1. tl
				if x > 0 and y > 0 and grid[x-1][y-1] == 1:
					n += 1
				# 2. t
				if y > 0 and grid[x][y-1] == 1:
					n += 1
				# 3. tr
				if x < width-1 and y > 0 and grid[x+1][y-1] == 1:
					n += 1
				# 4. l
				if x > 0 and grid[x-1][y] == 1:
					n += 1
				# 5. r
				if x < width-1 and grid[x+1][y] == 1:
					n += 1
				# 6. bl
				if x > 0 and y < height-1 and grid[x-1][y+1] == 1:
					n += 1
				# 7. b
				if y < height-1 and grid[x][y-1] == 1:
					n += 1
				# 8. br
				if x < width-1 and y < height-1 and grid[x+1][y+1] == 1:
					n += 1
				
				if grid[x][y] == 1:
					changed  += 1
					if n < 2:
						grid[x][y] = 0
					elif n > 3 :
						grid[x][y] = 0
					else:
						grid[x][y] = 1
				elif n == 3:
					grid[x][y] = 1
					changed += 1
					
				#return changed > 0
					
	seed()
	while True:
		display()
		step()
		if buttons.is_triggered("BTN_A"):
			seed()
		
game_of_life()