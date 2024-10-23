from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
class MyApp(App):
    def build(self):
        layout=FloatLayout()
        label1=Label(text="NAME:",pos_hint={'center_x':0.17,"center_y":0.7})
        label2=Label(text="TABLE NO:",pos_hint={'center_x':0.15,"center_y":0.5})
        textinput1=TextInput(size_hint=(None,None),width=200,height=50,pos_hint={'center_x':0.5,"center_y":0.7})
        textinput2=TextInput(size_hint=(None,None),width=200,height=50,pos_hint={'center_x':0.5,"center_y":0.5})
        btn1=Button(text='SUBMIT',size_hint=(None,None),width=100,height=50,pos_hint={'center_x':0.6,"center_y":0.3})
        btn2=Button(text='QUIT',size_hint=(None,None),width=100,height=50,pos_hint={'center_x':0.35,"center_y":0.3})
        layout.add_widget(label1)
        layout.add_widget(textinput1)
        layout.add_widget(label2)
        layout.add_widget(textinput2)
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        return layout


MyApp().run()