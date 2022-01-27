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

    def buyFood(self, food:Food, player: Player):
        
        if player.balance - food.price <= 0:
            print('당신의 잔고는 %d 입니다.' % player.balance)
            print('%s의 가격은 %d입니다.' %(food.name,food.price))
            print('잔고가 %d만큼 부족해서 살 수 없습니다.' %(food.price - player.balance))
        else:
            player.subMoney(food.price)
            print('%s를 구입했습니다.' % food.name)
            player.addInventory(food)