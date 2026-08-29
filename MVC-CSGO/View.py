import tkinter as tk
from functools import partial
from Controller import Controller

# view -> interface call user
class View:
    def __init__(self):
        self.controller = Controller()
        
        # main window interface
        self.app = tk.Tk()
        self.app.geometry("400x300")
        
        # Build widget and place on window
        self.icontext = "CSGO (Computer Science's Go)"
        self.sourceCodeCSGO = ""
    
    def init(self):
        # Build widget and place on window
        # Set icon
        # input to call system
        self.app.title(self.icontext)
        self.scText = tk.Text(self.app, width= 400, height= 15)
        self.scText.place(y=10)
        tk.Button(self.app, text = "Solution1", command = self._input1).place(x = 130,y = 260)
        tk.Button(self.app, text = "Solution2", command = self._input2).place(x = 210,y = 260)
        #tk.Entry(self.app, textvariable = self.sourceCodeCSGO, width = 300).place(x=0, y=0, width=400, height=50)
        # show window
        self.app.mainloop() 
    
    def _input1(self):
        self.controller.lexer1(self.scText.get(1.0, "end-1c"))
        
    def _input2(self):
        self.controller.lexer2(self.scText.get(1.0, "end-1c"))
    
    def getSoureCode():
        return self.scText.get(1.0, "end-1c"), self.solv