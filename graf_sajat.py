import queue

class Graf:
    def __init__(self, iranyitott = False):
        self.elek = []
        self.iranyitott = iranyitott
        self.csucsok = []

    def beszur_pont(self, p):
        if p not in self.csucsok:
            self.csucsok.append(p)
    
    def beszur_el(self, el):
        if el not in self.elek:
            self.elek.append(el)

    def szomszedok(self, p):
        szomszedok_pontok = []
        for i in self.elek:
            if p in i:
                res = [j for j in i if j != p] 
                szomszedok_pontok.append(res[0])
        
        return szomszedok_pontok
    
    def szelessegi_bejaras(self, kiindulopont):
        sor = queue.Queue()
        sor.put(kiindulopont)
        feldolgozott = []
        feldolgozott.append(kiindulopont)
        while sor.qsize() > 0:
            pont = sor.get()
            for i in self.szomszedok(pont):
                if i not in feldolgozott:
                    sor.put(i)
                    feldolgozott.append(i)
        
        return feldolgozott

    def melysegi_bejaras(self, kiindulopont, feldolgozott):
        feldolgozott.append(kiindulopont)
        for i in self.szomszedok(kiindulopont):
            if i not in feldolgozott:
                self.melysegi_bejaras(i, feldolgozott)

        return feldolgozott

csucsok = [2, 1, 3, 4, 5, 6, 7]
elek = [[1, 2], [1, 5], [1, 4], [2, 3], [4, 3], [4, 6], [3, 6], [6, 7]]

g = Graf()
for i in csucsok:
    g.beszur_pont(i)

for i in elek:
    g.beszur_el(i)

g.csucsok
g.elek

feldolgozott = []
kiindulopont = 2
g.melysegi_bejaras(kiindulopont, feldolgozott)

g.szelessegi_bejaras(2)