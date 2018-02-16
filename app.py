import pygame
from screen import Screen
import button
import pointer
import cursor



class app:
	def __init__(self, handler):

		self.handler = handler
		self.current_state
		self.display_width = 1440
		self.display_height = 720
		self.display = Screen.new(self.display_width, self.display_height, white, "Tilemaker")


	def get_current_state(self):
		return self.current_state

	def set_current_state(self, cs):
		self.current_state = cs

	def init_state(self):
		#this state will be the first thing users see atm	