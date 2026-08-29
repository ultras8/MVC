# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from functools import partial
from Controller import Controller
from tkinter import ttk
class Elderly:
    def __init__(self,master):
        master.withdraw()
        usernameInput = tk.StringVar()
        passwordInput = tk.StringVar()
        elderlyWindow = Toplevel(master)
        elderlyWindow.geometry("400x400")
        Label(elderlyWindow, text = "Username",font=("Arial", 35) ).pack()
        Entry(elderlyWindow, textvariable = usernameInput).pack()
        Label(elderlyWindow, text = "Password",font=("Arial", 35) ).pack()
        Entry(elderlyWindow, textvariable = passwordInput).pack()
        paramExit = partial(self._exit,master,elderlyWindow)
        paramSub = partial(self._submit,usernameInput,passwordInput,elderlyWindow)
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 15))
        Button(elderlyWindow,text="Submit",command=paramSub,width=10, style="TButton").pack()
        Button(elderlyWindow,text="Home",command=paramExit,width=10, style="TButton").pack()
    def _exit(self,master,elderlyWindow):
        master.deiconify()
        elderlyWindow.withdraw()
    def _submit(self,user,password,elderlyWindow):
        cont = Controller()
        if(cont.gui_init(user.get(),password.get()) == 1):
            Label(elderlyWindow, text = "เข้าสู่ระบบสำเร็จ" ,font=("Arial", 35)).pack()
        else:
            Label(elderlyWindow, text = "เข้าสู่ระบบล้มเหลว" ,font=("Arial", 35)).pack()