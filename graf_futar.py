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

    def futar_bejaras(self, kiindulopont, feldolgozott, lepes_szam):
        feldolgozott.append(kiindulopont)
        if lepes_szam > 0:
            lepes_szam -= 1
            for i in self.szomszedok(kiindulopont):
                if i not in feldolgozott:
                    self.futar_bejaras(i, feldolgozott, lepes_szam)

        return feldolgozott    

# region tavolsag proba
#     def tavolsag(self, kiindulopont):
#         L = []
#         feldolgozott = []
#         for i in range(len(self.csucsok)):
#             L.append(float('inf'))
# 
#         L[kiindulopont - 1] = 0
#         tavolsag = 1
#         feldolgozott.append(kiindulopont)
#         for i in self.szomszedok(kiindulopont):
#             L[i - 1] = tavolsag
#             self.seged(i, tavolsag, L, kiindulopont, feldolgozott)
# 
#         return L
# 
#     def seged(self, csucs, tavolsag, L, kiindulopont, feldolgozott):
#         tavolsag += 1
#         feldolgozott.append(csucs)
# 
#         for i in self.szomszedok(csucs):
#             if i not in feldolgozott:
#                 if i != kiindulopont:
#                     if L[i - 1] >= tavolsag:
#                         L[i - 1] = tavolsag
#                     self.seged(i, tavolsag, L, kiindulopont, feldolgozott)
# 
#             
#     def tavolsag2(self, kiindulopont):
#         tavolsagok = []
#         sor = queue.Queue()
#         
#         for i in range(len(self.csucsok)):
#             tavolsagok.append(float('inf'))
#         
#         for i in self.szelessegi_bejaras(kiindulopont):
#             sor.put(i)
# 
#         tavolsag = 0
#         tavolsagok[kiindulopont - 1] = tavolsag
#         
#         while sor.qsize() > 0:
#             u = sor.get()
#             for i in self.szomszedok(u):
#                 if tavolsagok[i - 1] > tavolsag:
#                     tavolsagok[i - 1] = tavolsag
# 
#             tavolsag += 1
#         
#         return tavolsagok
#             
#     def futar_bejaras2(self, kiindulopont, feldolgozott, lepes_szam):
#         L = []
#         for i in range(len(self.csucsok)):
#             L.append(float('inf'))
# 
#         L[kiindulopont - 1] = 0
#         tavolsag = 1
#         
#         sor = queue.Queue()
#         sor.put(kiindulopont)
#         
#         feldolgozott = []
#         feldolgozott.append(kiindulopont)
# 
#         while sor.qsize() > 0:
#             pont = sor.get()
#             for i in self.szomszedok(pont):
#                 if i not in feldolgozott:
#                     sor.put(i)
#                     feldolgozott.append(i)
#                     if tavolsag < L[i - 1]:
#                         L[i - 1] = tavolsag
#         
#         return feldolgozott
# 
# endregion

#region Gráf szélességi és mélységi bejárása
# csucsok = [2, 1, 3, 4, 5, 6, 7]
# elek = [[1, 2], [1, 5], [1, 4], [2, 3], [4, 3], [4, 6], [3, 6], [6, 7]]
# 
# g = Graf()
# for i in csucsok:
#     g.beszur_pont(i)
# 
# for i in elek:
#     g.beszur_el(i)
# 
# g.csucsok
# g.elek
# 
# feldolgozott = []
# kiindulopont = 2
# g.melysegi_bejaras(kiindulopont, feldolgozott)
# 
# g.szelessegi_bejaras(2)
#endregion


bemenet = input()
varosok_szama = int(bemenet.split()[0])
bejarhato_tavolsag = int(bemenet.split()[1])
elek_szama = int(bemenet.split()[2])

g = Graf()

for i in range(1, varosok_szama + 1):
    g.beszur_pont(i)

for i in range(elek_szama):
    el = input()
    g.beszur_el([int(el.split()[0]), int(el.split()[1])])

utolso_sor = input()
kiindulopontok = [int(utolso_sor.split()[0]), int(utolso_sor.split()[1])]

eljutott = []
for i in kiindulopontok:
    feldolgozott = []
    for j in g.futar_bejaras(i, feldolgozott, bejarhato_tavolsag):
        if j not in eljutott:
            eljutott.append(j)

nem_jutott_el = []
for i in g.csucsok:
    if i not in eljutott:
        nem_jutott_el.append(i)

nem_jutott_el

g.tavolsag(1)