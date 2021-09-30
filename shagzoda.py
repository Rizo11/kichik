from aylana import *
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
