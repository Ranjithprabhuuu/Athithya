from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
class MyApp(App):
    def build(self):
        label1=Label(text="NAME:",font_size="40sp",bold=True,color=(190,0,200,1))
        btn1=Button(text="SUBMIT",size_hint=(0.3,0.4),pos_hint={"center_x":0.5,"center_y":0.5},font_size="20sp",on_press=self.btn_click)
        return btn1
    def btn_click(self):
        pass
MyApp().run()