import kivy 
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.graphics import Rectangle 
from kivy.graphics import Line 
from kivy.graphics import Color

class Touch(Widget):
	def __init__(self ,**kwargs):
		super(Touch , self).__init__(**kwargs)

		with self.canvas :
			Color(0, 1, 0, 0.5 , mode = 'rgba')
			Line(points =(20, 30 , 400 , 60  , 500))
			Color(1, 0, 0, 0.5 , mode= 'rgba')
			self.rect = Rectangle(pos = (50 ,50), size = (50 , 50))

	def on_touch_down(self, touch):
		self.rect.pos = touch.pos
		print("mouse down" , touch)

	def on_touch_move(self , touch):
		self.rect.pos = touch.pos
		print("mouse move" , touch)

class MyGrid(App):
	def build(self):
		return Touch()

if __name__ == "__main__":
	MyGrid().run()