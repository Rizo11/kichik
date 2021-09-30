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