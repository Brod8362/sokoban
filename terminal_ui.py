from blessings import Terminal
from urwid.curses_display import Screen
import blessings
from contextlib import contextmanager
t = Terminal()
class UI():
	def __init__(self):
		self.scr = Screen()
		self.t = Terminal()

	@contextmanager
	def setup(self):
		with self.t.hidden_cursor():
			with self.scr.start():
				self.scr.s.refresh()
				yield	

	def get_input(self):
		return self.scr.get_input()[-1]
	def draw_entity_at(self,ent,x=None,y=None): #add specifc cords later
		with t.location(ent.x, ent.y):
			if ent.checkSatisfied():
				print(t.red(ent.appearance))
			else:
				print(ent.appearance)
		
