import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
	name = ObjectProperty(None)
	lastname = ObjectProperty(None)
	email = ObjectProperty(None)

	def btn(self):
		print("name:" , self.name.text , "lastname :" , self.lastname.text , "email :" , self.email.text )
		self.name.text = ""
		self.lastname.text  = ""
		self.email.text = ""


def btn(instance):
	print("Run!")

class MyApp(App):
	def build(self):
		return MyGrid()


if __name__  == "__main__":
	MyApp().run()