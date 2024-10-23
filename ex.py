from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.tabbedpanel import TabbedPanel
Window.clearcolor=(1/255.0,70/255.0,70/255.0,1)
Window.size=(360,600)
class MyLayout(TabbedPanel):
    pass
class MeApp(App):
    def build(self):
        pass


class MyInterface(Widget):
     pass
MyApp().run()