import kivy 
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.popup import Popup

def show_popup():
	show = popup()
	show.popup()

	PopupWindow = Popup(title ="Popup Window" , content = show , size_hint = (None ,None) , size = (400, 400))
	PopupWindow.open()


class Widgets(Widget):
	def btn(self):
		show_popup()

class popup(FloatLayout):
	pass

class MyApp(App):
	def build(self):
		return Widgets()

		

if __name__ == "__main__":
	MyApp().run()
