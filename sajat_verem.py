class Verem:
    elemek=[]
    def ures(self):
        self.elemek = []
    
    def ures_e(self):
        return len(self.elemek) == 0
    
    def verembe(self, mit):
        self.elemek.insert(0, mit)
    
    def teto(self):
        return self.elemek[0]
    
    def verembol(self):
        if self.ures_e():
            return print("a veremnek nincs legfelső eleme")
        else:
            return self.elemek.pop(0)


s = Verem()
for i in range(5):
    s.verembe(i)
print(s.teto())
while not s.ures_e():
    print(s.verembol())