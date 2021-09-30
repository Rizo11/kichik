from math import *
class nuqta():
    """public propertylari: x:int, y:int
    konstruktorida x va y ni qabul qilib propertylarga joylay
    public methodlari: gachaMasofa() → ushbu method boshqa bir
    nuqta qabul qiladi joriy nuqtadan o'sha berilgan nuqtagacha
     bo'lgan masofani float sifatida qaytaradi"""

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    
    def gachaMasofa(self, n):
        return sqrt(abs(n.x - self.x)**2 + abs(n.y - self.y)**2)

class aylana():
    """public propertylari: markaz:Nuqta, radius:int
    - public methodlari: kesibUtadimi() → Aylana qabul qiladi va
     shaxzoda shu aylanani kesib o'tsa True yo'qsa False qaytaradi"""

    def __init__(self, markaz:nuqta, radius:int):
        self.markaz = markaz
        self.radius = radius
    
    def niIchidami(self, dot:nuqta):
        if dot.gachaMasofa(self.markaz) < self.radius:
            return True
        else:
            return False

class Shaxzoda():
    """public propertylari: start:Nuqta, end:Nuqt
    - public methodlari: kesibUtadimi() → Aylana qabul qiladi va
     shaxzoda shu aylanani kesib o'tsa True yo'qsa False qaytaradi"""

    def __init__(self, start:nuqta, end:nuqta):
        self.start = start
        self.end = end
    
    def kesibUtadimi(self, circle:aylana):
        if circle.niIchidami(self.start) or circle.niIchidami(self.end):
            return True
        else:
            return False



t_case = int(input())
for i in range(t_case):
    x, y, w, z = map(int, input().split())
    nuqta1 = nuqta(x, y)
    nuqta2 = nuqta(w, z)
    prince = Shaxzoda(nuqta1, nuqta2)
    n = int(input())
    counter = 0
    for j in range(n):
        a, b, r = map(int, input().split())
        a_nuqta = nuqta(a, b)
        circle = aylana(a_nuqta, r)
        if prince.kesibUtadimi(circle):
            counter += 1
    print(counter)
    
""" 0 0 1 1
8
0 0 1
1 1 0
2 2 2
1 1 1
2 2 2
12 1 1
12 1 2
-5 1 5   """    