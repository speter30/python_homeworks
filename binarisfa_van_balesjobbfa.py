class TBinfaElem:
    def __init__(self):
        self.gyoker = None
        self.bal = None
        self.jobb = None

    def bal_gyerek(self):
        if self.bal != None:
            return self.bal
        return "üres"

    def jobb_gyerek(self):
        if self.jobb != None:
            return self.jobb
        return "üres"

    def level_eleme(self):
        return self.bal == None and self.jobb == None

    def ures_e(self):
        return self.gyoker == None

    def beszuras(self, ertek):
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
                            self.bal.beszuras(ertek)
                    else:
                        if self.jobb == None:
                            elem = TBinfaElem()
                            elem.gyoker = ertek
                            self.jobb = elem
                        else:
                            self.jobb.beszuras(ertek)
    
    def pre_order_bejaras (self):
        if self != None:
            print(self.gyoker)
            if self.bal_gyerek() != "üres":
                self.bal_gyerek().pre_order_bejaras()
            if self.jobb_gyerek() != "üres":
                self.jobb_gyerek().pre_order_bejaras()
    
    def post_order_bejaras(self):
        if self != None:
            if self.bal_gyerek() != "üres":
                self.bal_gyerek().post_order_bejaras()
            if self.jobb_gyerek() != "üres":
                self.jobb_gyerek().post_order_bejaras()
            print(self.gyoker)
    
    def in_order_bejaras(self):
        if self != None:
            if self.bal_gyerek() != "üres":
                self.bal_gyerek().in_order_bejaras()
            print(self.gyoker)
            if self.jobb_gyerek() != "üres":
                self.jobb_gyerek().in_order_bejaras()  

    def csomopontok_szama(self):
        szamlalo = 0
        if self != None:
            if self.bal_gyerek() != "üres" and self.jobb_gyerek() != "üres":
                szamlalo += 1

            if self.bal_gyerek() != "üres":

                szamlalo = szamlalo + self.bal_gyerek().csomopontok_szama()
            if self.jobb_gyerek() != "üres":
                szamlalo = szamlalo + self.jobb_gyerek().csomopontok_szama()   

        return szamlalo

#elemek= [50, 24, 64, 12, 31, 58, 71]
#
#fa = TBinfaElem()
#fa.gyoker
#
#for i in elemek:
#    fa.beszuras(i)
#
#print(fa.gyoker)
#print(fa.bal_gyerek().bal_gyerek().gyoker)
#print(fa.jobb_gyerek().bal_gyerek().gyoker)
#print(fa.bal_gyerek().bal_gyerek().level_eleme())
#
#print(fa.pre_order_bejaras())
#print(fa.post_order_bejaras())
#print(fa.in_order_bejaras())
#
#print(fa.csomopontok_szama())

elemek2 = [11, 6, 19, 4, 8, 17, 43, 5, 10, 31, 49]
fa2 = TBinfaElem()

for i in elemek2:
    fa2.beszuras(i)

print(fa2.pre_order_bejaras())
#print(fa2.post_order_bejaras())
#print(fa2.in_order_bejaras())
#print(fa2.csomopontok_szama())