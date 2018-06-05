#!/usr/bin/env python
#encoding: utf8
#vim: et: sw=4: ts=4: ai: si: sta

import pdb
import sys
try:
	from pygame_ui import UI
except:
	from terminal_ui import UI
	pass
ui = UI()
boardwidth = 8#actual width 
boardheight = 9 #actual height 
entities = []
impassible = [1]
solveable = [4,5]
clearspace = u" "
graphicsreference = {
0: clearspace,
1: u"\u2588",
2: clearspace,
3: clearspace,
4: u"x",
5: u"x",
}
boxgraphic = u"\u25A0"
playergraphic = u"\u263A"
"""IDs reference
0. Air
1. Wall
2. Player Spawn
3. Box Spawn
4. Box Destination
"""
class Map():
	def __init__(self):
		self.board = [0,0,1,1,1,1,1,0,
			      1,1,1,0,0,0,1,0,
			      1,4,2,3,0,0,1,0,
			      1,1,1,0,3,4,1,0,
			      1,4,1,1,3,0,1,0,
			      1,0,1,0,4,0,1,1,
			      1,3,0,5,3,3,4,1,
			      1,0,0,0,4,0,0,1,
			      1,1,1,1,1,1,1,1]
	def get(self):
		return self.board

	def __iter__(self):
		return iter(self.board)
	def __getitem__(self, xy):
		x,y, = xy #plx+x, ply+y
		listPos = (boardwidth*y)+x
		return self.board[listPos]
class Player():
	def __init__(self):
		self.x = plyspnx
		self.y = plyspny
		self.map = plymap
		self.appearance = playergraphic
	def draw(self):
		ui.draw_entity_at(self)
	def locate(self):
		return self.x,self.y
	def move(self, x, y):
		tile = self.map[self.x+x, self.y+y] 
		if tile in impassible:
			return	
		elif tile not in impassible:
			pass
		for ent in entities:
			if ent.pushable():
				if ent.x == self.x+x and ent.y == self.y+y:
					if ent.move(x,y) == True:
						pass
					else:
						return False
				
		self.x += x
		self.y += y
	def checkSatisfied(self):
		return False
	def isBox(self):
		return False
		
class Box():
	def __init__(self, x, y, map):
		self.x = x
		self.y = y
		self.map = map
		self.appearance = boxgraphic
	def draw(self):
		ui.draw_entity_at(self)
	def move(self, x, y):
		tile = self.map[self.x+x, self.y+y]
		if tile in impassible:
			return False
		elif tile not in impassible:
			pass
		for ent in entities: 
			if ent.pushable():
				if ent.x == self.x+x and ent.y == self.y+y:
					if ent.move(x,y) != True:
						return False
		self.x += x
		self.y += y
		return True
	def pushable(self):
		return True
	def checkSatisfied(self):
		tile = self.map[self.x, self.y]
		if tile not in solveable:
			return False
		return True
	def isBox(self):
		return True
curx = 0
cury = 0
plyspnx = 0
plyspny = 0
gb = Map()
plymap = gb
def draw():
	ui.clear()
	global curx
	global cury
	curx = 0
	cury = 0
	for x in gb.board:
		ui.draw_tile_at(x,curx,cury,graphicsreference)
		curcontrol()
def spawn_entites():
	global curx
	global cury
	curx = 0
	cury = 0
	for x in gb.board:
		if x == 2:
			global plyspnx
			global plyspny
			plyspnx = curx
			plyspny = cury
		elif x == 3:
			entities.append(Box(curx,cury,gb))
		elif x == 5: 
			entities.append(Box(curx,cury,gb))
		curcontrol()
def curcontrol():
	global curx 
	global cury
	curx += 1
	if curx == boardwidth:
		curx = 0
		cury += 1
		return
	if cury == boardheight: 
		return 

def checkComplete():
	for ent in entities:
		if ent.isBox() and not ent.checkSatisfied():
			return False
	print('victory')
	sys.exit()
	 

spawn_entites()
player = Player()
ui.music()
with ui.setup():
	while True:
		draw()
		player.draw()
		for ent in entities:
			ent.draw()
		ui.update()
		inp = ui.get_input()	
		if inp == "d":
			player.move(1,0)
		if inp == "a":
			player.move(-1,0)
		if inp == "w":
			player.move(0,-1)
		if inp == "s":
			player.move(0,1)
		if inp == "n":
			player.move(0,0)
		checkComplete()
