from ClassFood import *
from ClassCat import *
#플레이어
# 플레이어가 아이템을 살 때 필요한 돈
# 속성
# balance
# 기능
# addMoney
# subMoney
#  
#
#

class Player:
    balance = 0
    playerInventory = []
    def __init__(self,name):
        self.name = name

    def addMoney(self,money):
        self.balance = self.balance + money
        
    def subMoney(self,money):
        if self.balance - money <= 0:
            print("돈이 부족합니다!")
        else:
            self.balance = self.balance - money
            print('%d만큼의 돈이 빠져나가고\n잔고가 %d만큼 남아있습니다' % money,self.balance)

    def addInventory(self, food:Food):
        
        self.playerInventory.append(food.name)
        
        print('인벤토리에 %s이(가) 추가되었습니다!' % food.name)
        
    #def showInventory(self):
    #   
    #   if len(self.playerInventory) == 0:
    #       print('아무것도 소지하고 있지 않습니다.')
    #   
    #   else: 
    #       print(self.playerInventory)   

    def feed(self):

        self.whatIHave = input('어떤 음식을 주겠습니까? : ')
        
        if self.whatIHave not in self.playerInventory:
            print('''"%s"을(를) 소지하고 있지 않습니다.''' % self.whatIHave)
        
        else:
            self.playerInventory.remove(self.whatIHave)
            print('%s을(를) 주었습니다.' % self, self.whatIHave)
            