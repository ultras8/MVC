import tkinter as tk
import tkinter.messagebox
from Model import Model

class Controller:
    def __init__(self):
        self.model = Model()
        self.lex1 = []
        self.lex2 = []
        
    
    def lexer1(self, sc):
        self.value1 = []
        line1 = sc.splitlines()
        for i in line1:
            if not (i[0] == "/" and i[1] == "/"):
                word1 = i.split()
                keyword1 = self.model.getKeyword1()
                for key in keyword1:
                    if key in word1 and word1[0] == "declare":
                        key1 = word1.pop(0)
                        key2 = word1.pop(0)
                        self.lex1.append(key1+" is Keyword")
                        self.lex1.append(key2+" is Identifier")
                        self.value1.append(key2)
                        if len(word1) > 0:
                            self.iden1(word1,self.value1)
                    else :
                        self.iden1(word1,self.value1)
        self.toString(self.lex1)
                            
    def iden1(self, word1, value):
        for i in range (len(word1)):
            if word1[i] == '=':
                self.lex1.append(word1[i]+" is Symbol")
            elif word1[i] in self.model.getsymbol():
                self.lex1.append(word1[i]+" is Symbol")
            elif word1[i] in value:
                self.lex1.append(word1[i]+" is Identifier")
            elif word1[i].isdigit():
                self.lex1.append(word1[i]+" is Literal")
            elif "." in word1[i]:
                tmp = split(".")
                tmp[0].isdigit()
                self.lex2.append(word1[i]+" is Literal")
            else :
                self.exceptionErrorPrint()
                
    def lexer2(self, sc):
        self.value2 = []
        line2 = sc.splitlines()
        for i in line2:
            if not (i[0] == "/" and i[1] == "/"):
                word2 = i.split()
                keyword2 = self.model.getKeyword2()
                for key in keyword2:
                    if key in word2 and word2[0] == "declare":
                        key1 = word2.pop(0)
                        key2 = word2.pop(0)
                        self.lex2.append(key1+" is Keyword and Sign")
                        self.lex2.append(key2+" is Variable")
                        self.value2.append(key2)
                self.iden2(word2,self.value2)
        self.toString(self.lex2)
    
    def iden2(self, word2, value):
        for i in range (len(word2)):
            if word2[i] == '=':
                self.lex2.append(word2[i]+" is Assignment")
            elif word2[i] in self.model.getAssignment():
                self.lex2.append(word2[i]+" is Assignment")
            elif word2[i] in value:
                self.lex2.append(word2[i]+" is Variable")
            elif word2[i].isdigit():
                self.lex2.append(word2[i]+" is Integer")
            elif "." in word2[i]:
                tmp = split(".")
                tmp[0].isdigit()
                self.lex2.append(word2[i]+" is Floating")
            elif word2[i] in self.model.getKeyword2():
                self.lex2.append(word2[i]+" is Keyword and Sign")
            else :
                self.exceptionErrorPrint()
            
                
    def toString(self,lex):              
        for i in lex:
            print(i)
                        
    def exceptionErrorPrint(self):
        tk.messagebox.showerror("Error","Error Source Code")
                
            
        