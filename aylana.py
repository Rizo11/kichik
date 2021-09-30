from nudta import *
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