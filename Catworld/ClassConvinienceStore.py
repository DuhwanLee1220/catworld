from ClassFood import *
from ClassPlayer import Player

# food를 파는곳
# 구매했던 음식을 되팔 수 없음.
# 편의점
class ConvinienceStore:
    def __init__(self,name):
        self.name = name
        self.sellList=[]

    def addItem(self,food:Food):
        
        self.sellList.append(food.name)

    def printSellList(self):
        i = 1
        for products in self.sellList:
            print('%d. %s' % (i,products))
            i += 1
        print("구매할 물건을 선택해주세요")
