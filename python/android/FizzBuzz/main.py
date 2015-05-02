# -*- coding:UTF8 -*-

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '300')

from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import BooleanProperty
from kivy.properties import NumericProperty
from kivy.app import App

Builder.load_string('''
#:kivy 1.8.0

<FizzBuzz>:
    BoxLayout:
        orientation: 'vertical'
        pos: root.pos
        size: root.size

        Label:
        	text: ' ' if root.G_over else root.system
        	font_size: 30

        Label:
            text: str(root.num)
            font_size: 120

        BoxLayout:
            orientation: 'horizontal'
            size_hint: 1.0, 1.0

            Button:
                text: 'next'
                font_size: 30
                on_press: root.on_command('next')

            Button:
                text: 'Fizz'
                font_size: 30
                on_press: root.on_command('Fizz')

            Button:
                text: 'Buzz'
                font_size: 30
                on_press: root.on_command('Buzz')

            Button:
            	text: 'FizzBuzz'
            	font_size: 30
            	on_press: root.on_command('FizzBuzz')

            Button:
            	text: 'reset'
            	font_size: 25
            	center_x: (root.width/3)
            	on_press: root.on_reset()
''')

class FizzBuzz(Widget):
	system='GameOver'
	G_over = BooleanProperty(True)
	num = NumericProperty(1)

	def answer(self,a_num,string):
		if self.G_over == False:
			return False

		if string is 'next':
			if a_num%3==0 or a_num%5==0:
				return False
			else:
				return True
		elif string is 'Fizz':
			if a_num%3==0 and a_num%5!=0:
				return True
			else:
				return False
		elif string is 'Buzz':
			if a_num%5==0 and a_num%3!=0:
				return True
			else:
				return False
		elif string is 'FizzBuzz':
			if a_num%3==0 and a_num%5==0:
				return True
			else:
				return False


	def on_command(self,command):
		if command == 'next':
			if self.answer(self.num,'next'):
				self.num+=1
			else:
				self.G_over = False
		elif command == 'Fizz':
			if self.answer(self.num,'Fizz'):
				self.num+=1
			else:
				self.G_over = False
		elif command == 'Buzz':
			if self.answer(self.num,'Buzz'):
				self.num+=1
			else:
				self.G_over = False
		elif command == 'FizzBuzz':
			if self.answer(self.num,'FizzBuzz'):
				self.num+=1
			else:
				self.G_over = False

	def on_reset(self):
		self.G_over = True
		self.num = 1


class FizzBuzzApp(App):
	def build(self):
		return FizzBuzz()

if __name__ == '__main__':
	FizzBuzzApp().run()


