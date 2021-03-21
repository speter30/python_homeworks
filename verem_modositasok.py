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
    
    def utolso_torlese(self):
        if self.ures_e():
            return print("a verem üres")
        else:
            seged = []
            for i in range (len(self.elemek) - 1):
                seged.append(self.verembol())
            self.verembol()
            for i in reversed(seged):
                self.verembe(i)
            return self

    def n_torlese(self, n):
        if len(self.elemek) < n:
            return print("a megadott szám nagyobb, mint a verem mélysége")
        else: 
            seged = []
            for i in range (n-1):
                seged.append(self.verembol())
            self.verembol()
            for i in reversed(seged):
                self.verembe(i)
            return self

    def masodik_torlese(self):
        if self.ures_e() or len(self.elemek) == 1:
            return print("nincs második elem")
        else:
            seged = self.elemek.pop(0)
            self.verembol()
            self.verembe(seged)
            #self.n_torlese(2)
            return self
            
    
    def tartalom(self):
         for i in self.elemek:
             print(i)


s = Verem()
for i in range(6):
    s.verembe(i)
#print(s.teto())
print(s.tartalom())
print("------")
s.n_torlese(10)
print("------")
print(s.tartalom())