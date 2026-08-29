
# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from functools import partial
from Controller import Controller
class Child:
    def __init__(self,master):
        master.withdraw()
        usernameInput = tk.StringVar()
        passwordInput = tk.StringVar()
        childWindow = Toplevel(master)
        Label(childWindow, text = "Username" ).pack()
        Entry(childWindow, textvariable = usernameInput).pack()
        Label(childWindow, text = "Password" ).pack()
        Entry(childWindow, textvariable = passwordInput).pack()
        paramExit = partial(self._exit,master,childWindow)
        paramSub = partial(self._submit,usernameInput,passwordInput,childWindow)
        Button(childWindow,text="Submit",command=paramSub).pack()
        Button(childWindow,text="Home",command=paramExit).pack()
    def _exit(self,master,childWindow):
        master.deiconify()
        childWindow.withdraw()
    def _submit(self,user,password,childWindow):
        cont = Controller()
        if(cont.gui_init(user.get(),password.get()) == 1):
            Label(childWindow, text = "เข้าสู่ระบบสำเร็จ" ).pack()
        else:
            Label(childWindow, text = "เข้าสู่ระบบล้มเหลว" ).pack()