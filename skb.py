#!/usr/bin/env python
# coding: utf8
#vim: et: sw=4: ts=4: ai: si: sta

from blessings import Terminal 
from urwid.curses_display import Screen
import blessings
import pdb
import sys
t = Terminal()
scr = Screen()
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
		self.plyx = plyspnx
		self.plyy = plyspny
		self.map = plymap
	def draw(self):
		with t.location(self.plyx, self.plyy):
			print(t.blue(playergraphic))
	def locate(self):
		return self.plyx,self.plyy
	def move(self, x, y):
		tile = self.map[self.plyx+x, self.plyy+y] 
		if tile in impassible:
			return	
		elif tile not in impassible:
			pass
		for ent in entities:
			if ent.pushable():
				if ent.x == self.plyx+x and ent.y == self.plyy+y:
					if ent.move(x,y) == True:
						pass
					else:
						return False
				
		self.plyx += x
		self.plyy += y
		
class Box():
	def __init__(self, x, y, map):
		self.x = x
		self.y = y
		self.map = map
	def draw(self):
		with t.location(self.x, self.y):
			if self.checkSatisfied():
				print(t.red(boxgraphic))
			else:
				print(boxgraphic)
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
	print(t.clear())
	global curx
	global cury
	curx = 0
	cury = 0
	for x in gb.board:
		with t.location(curx, cury):
			print(graphicsreference[x])
			curcontrol()
def spawn_entites():
	global curx
	global cury
	curx = 0
	cury = 0
	for x in gb.board:
		with t.location(curx, cury):
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
with t.hidden_cursor():
	with scr.start():
		scr.s.refresh()
		while True:
			draw()
			player.draw()
			for ent in entities:
				ent.draw()	
			for i in scr.get_input():
				inp = i
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
