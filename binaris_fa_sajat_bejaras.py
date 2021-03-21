class TBinfaElem:
    def __init__(self):
        self.gyoker = None
        self.bal = None
        self.jobb = None

    def BalGyerek(self):
        if self.bal != None:
            return self.bal
        return "üres"

    def JobbGyerek(self):
        if self.jobb != None:
            return self.jobb
        return "üres"

    def leveleleme(self):
        return self.bal == None and self.jobb == None

    def urese(self):
        return self.gyoker == None

    def Beszuras(self, ertek):
            if self == None:
                self.gyoker = ertek
            else:
                if self.gyoker == None:
                    self.gyoker = ertek
                else:
                    if self.gyoker >= ertek: 
                        if self.bal == None:  
                            elem = TBinfaElem()
                            elem.gyoker = ertek
                            self.bal = elem
                        else:
                            self.bal.Beszuras(ertek)
                    else:
                        if self.jobb == None:
                            elem = TBinfaElem()
                            elem.gyoker = ertek
                            self.jobb = elem
                        else:
                            self.jobb.Beszuras(ertek)
    
    def preOrderBejaras (self):
        if self != None:
            print(self.gyoker)
            if self.BalGyerek() != "üres":
                self.BalGyerek().preOrderBejaras()
            if self.JobbGyerek() != "üres":
                self.JobbGyerek().preOrderBejaras()
    
    def postOrderBejaras(self):
        if self != None:
            if self.BalGyerek() != "üres":
                self.BalGyerek().postOrderBejaras()
            if self.JobbGyerek() != "üres":
                self.JobbGyerek().postOrderBejaras()
            print(self.gyoker)
    
    def inOrderBejaras(self):
        if self != None:
            if self.BalGyerek() != "üres":
                self.BalGyerek().inOrderBejaras()
            print(self.gyoker)
            if self.JobbGyerek() != "üres":
                self.JobbGyerek().inOrderBejaras()            

elemek= [50, 24, 64, 12, 31, 58, 71]

fa = TBinfaElem()
fa.gyoker

for i in elemek:
    fa.Beszuras(i)

print(fa.gyoker)
print(fa.BalGyerek().BalGyerek().gyoker)
print(fa.JobbGyerek().BalGyerek().gyoker)
print(fa.BalGyerek().BalGyerek().leveleleme())

print(fa.preOrderBejaras())
print(fa.postOrderBejaras())
print(fa.inOrderBejaras())