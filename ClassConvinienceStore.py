from ClassFood import *
from ClassPlayer import Player
from printer import *

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

        print('1. %s : 포만감 %d, 친밀감 %d, 체력 %d, 가격 %d' % (food1.name,food1.satiety,food1.affection,food1.healthPoint,food1.price))
        print('2. %s : 포만감 %d, 친밀감 %d, 체력 %d, 가격 %d' % (food2.name,food2.satiety,food2.affection,food2.healthPoint,food2.price))
        print('3. %s : 포만감 %d, 친밀감 %d, 체력 %d, 가격 %d' % (food3.name,food3.satiety,food3.affection,food3.healthPoint,food3.price))
        print('4. %s : 포만감 %d, 친밀감 %d, 체력 %d, 가격 %d' % (food4.name,food4.satiety,food4.affection,food4.healthPoint,food4.price))
        print('5. %s : 포만감 %d, 친밀감 %d, 체력 %d, 가격 %d' % (food5.name,food5.satiety,food5.affection,food5.healthPoint,food5.price))

        printInfo("구매할 물건을 선택해주세요")

    def buyFood(self, food:Food, player: Player):
        
        if player.balance - food.price < 0:
            printLaterFewSec(2)
            printLineFeed1('당신의 잔고는 %d 입니다.' % player.balance)
            printLineFeed1('%s의 가격은 %d입니다.' %(food.name,food.price))
            printLineFeed1('잔고가 %d만큼 부족해서 살 수 없습니다.' %(food.price - player.balance))
        else:
            printLineFeed1('%s를 구입했습니다.' % food.name)
            player.subMoney(food.price)
            printLaterFewSec(2)
            player.addInventory(food)
            printInfo('당신의 잔고는 %d 입니다.' % player.balance)