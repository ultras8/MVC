import tkinter as tk
from functools import partial
from Controller import Controller
from Child import Child
from Scholar import Scholar
from Elderly import Elderly

# view -> interface call user
class View:
    def __init__(self):
        self.controller = Controller()
        
        # main window interface
        self.app = tk.Tk()
        self.app.geometry("400x300")
        
        # Build widget and place on window
        self.icontext = "CSGO (Computer Science's Go)"
    
    def init(self):
        # Build widget and place on window
        # Set icon
        # input to call system
        self.app.title(self.icontext)
        pasrameterChild = partial(self._callUIChild,self.app)
        pasrameterScholar = partial(self._callUIScholar,self.app)
        pasrameterElderly = partial(self._callUIElderly,self.app)
        tk.Button(self.app,text="เด็ก",command=pasrameterChild,width=400,font=("Arial", 35)).pack()
        tk.Button(self.app,text="นักศึกษา", command= pasrameterScholar,width=400,font=("Arial", 35)).pack()
        tk.Button(self.app,text="ผู้สูงวัย", command= pasrameterElderly,width=400,font=("Arial", 35)).pack()    
        self.app.mainloop() 
        
        
    @staticmethod
    def _callUIChild(app):
        Child(app)
    @staticmethod    
    def _callUIScholar(app):
        Scholar(app)
    @staticmethod    
    def _callUIElderly(app):
        Elderly(app)