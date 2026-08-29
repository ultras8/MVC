class Model:
    def __init__(self):
        self.keyword1 = ["declare"]
        self.symbol = ["+","="]
        self.keyword2 = ["declare","+"]
        self.Assignment = ["="]
    
    def addKeyword1(self, word):
        self.keyword1.append(word)
    
    def addKeyword2(self, word):
        self.keyword2.append(word)
        
    def addsymbol(self, sym):
        self.symbol.append(sym)
    
    def addAssignment(self, sym):
        self.Assignment.append(sym)
        
    def delKeyword1(self, word):
        self.keyword1.remove(word)
    
    def delKeyword2(self, word):
        self.keyword2.remove(word)
        
    def delsymbol(self, sym):
        self.symbol.remove(sym)
    
    def delAssignment(self, sym):
        self.Assignment.remove(sym)
        
    def getKeyword1(self):
        return self.keyword1
    
    def getKeyword2(self):
        return self.keyword2
        
    def getsymbol(self):
        return self.symbol
    
    def getAssignment(self):
        return self.Assignment