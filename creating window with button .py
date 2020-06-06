import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyGrid(GridLayout):
	def __init__(self,**kwargs):
		super(MyGrid , self).__init__(**kwargs)
		self.cols = 1

		self.inside = GridLayout()
		self.inside.cols = 2

		self.inside.add_widget(Label(text ="First name:"))
		self.name = TextInput(multiline = False)
		self.inside.add_widget(self.name)

		self.inside.add_widget(Label(text = "Last name:"))
		self.lastname = TextInput(multiline = "false")
		self.inside.add_widget(self.lastname)

		self.inside.add_widget(Label(text = "email:"))
		self.email = TextInput(multiline = "false")
		self.inside.add_widget(self.email)

		self.add_widget(self.inside)

		self.submit = Button(text = "SUBMIT", font_size= 20)
		self.submit.bind(on_press =self.pressed)
		self.add_widget(self.submit)

	def pressed(self, instance):
		name = self.name.text
		lastname = self.lastname.text 
		email = self.email.text

		print("Name:",name, "Last name:", lastname ,"email:",email)
		self.name.text = ""
		self.lastname.text = ""
		self.email.text = ""

class simplekivy(App):
	def build(self):
		return MyGrid()

if __name__== "__main__" :
	simplekivy().run()