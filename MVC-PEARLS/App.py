from View import View
from Controller import Controller
class App:
    def __init__(self):
        self.view = View()
        self.cont = Controller()
        self.view.init()
        self.cont._setDateBase()