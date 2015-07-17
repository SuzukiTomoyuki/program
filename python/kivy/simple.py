# -*- coding:UTF8 -*-

from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition


class SimpleApp2(Screen):
	pass

class SimpleApp(Screen):
	pass

class ScreenManegement(ScreenManager):
	pass

kivy_langage = Builder.load_file("simple.kv")

class Simple(App):
	def build(self):
		return kivy_langage

if __name__ == "__main__":
	Simple().run()