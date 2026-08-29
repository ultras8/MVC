import tkinter as tk
from functools import partial
from Controller import Controller
import subprocess
import sys
#Scholar interface
class Scholar:
    def __init__(self,master):
        master.withdraw()
        print("username*")
        userName = input()
        print("password*")
        passWord = input()
        self._callController(userName,passWord,master)
   
    def _callController(self,userName,passWord,master):
        cont = Controller()
        print(userName)
        cont.scholar_init(userName,passWord,master)