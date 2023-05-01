from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from threading import Thread
from functools import partial
from main import *
import os


class imgpdfapp(App):
    def build(self):
        self.title("Image To Pdg application by adithyan")
        self.layout=GridLayout(cols=1,spacing=10)
        self.file_chooser=FileChooserListView()
        self.layout.add_widget(self.file_chooser)
        self.convertbutton=Button(text="convert",size_hint_y=None,height=50)
        self.convertbutton.bind(on_press=self.convert_image)
        self.layout.add_widget(self.convertbutton)
        return self.layout
    

def convert_image(self,instance):
    path=self.file_chooser.selection and self.file_chooser.selection[0]
    if not path:
        self.show_error("Please select the image to be converted")
        return
    self.convertbutton.disabled=True
    thread=Thread(target=self.convertto,args=(path,))
    thread.start()
    
def convertto(self,path):
    try:
        pdf_contents=convert(path)
        pdf_path=os.path.splitext(path)[0]+".pdf"
        with open(pdf_path,"wb") as f:
            f.write(pdf_contents) 
        Clock.schedule_once(partial(self.show_success,pdf_path))
    except Exception as e:
        Clock.schedule_once(partial(self.show_success,pdf_path))
def show_success(self,pdf_path,dt):
    popup=Popup(title="success",content=Button(text=f'pdf saved to {pdf_path}'),size_hint=(None,None),size=(400,200))
    popup.open()
def show_error(self,message,dt=None):
    popup=Popup(title="error",content=Button(text=message),size_hint=(None,None),size=(400,200))
    popup.open()

    
    



