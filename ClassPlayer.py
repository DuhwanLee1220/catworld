from ClassFood import *
from ClassCat import *
import random as rd
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
            print('%d만큼의 돈이 빠져나가고\n잔고가 %d만큼 남아있습니다' % (money,self.balance))

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
            print('%s을(를) 주었습니다.' % self.whatIHave)
    
    def touch(self,cat : Cat):
        
        if cat.affection <= 50:
            print('%s와 친밀감이 너무 낮아 쓰다듬을 수 없습니다' % cat.name)
        
        else:
            print('%s가 고로롱 소리를 내며 편안함을 느낍니다.' % cat.name)
            affectionUp = rd.randint(1,5)
            cat.affection += affectionUp
            print('%s와의 친밀감이 %d 만큼 상승하여 %d만큼의 친밀감을 갖고 있습니다.' %(cat.name, affectionUp, cat.affection))

    def stare(self,cat:Cat):
        
        print('%s를 지켜보고 있습니다...' %(cat.name))
        if cat.affection <= 50:
            affectionDown = rd.randint(1,5)
            print('%s가 시비를 거는거로 오해했습니다!\n%s와의 친밀감이 %d만큼 차감됩니다.\n현재 %s와의 친밀감 %d'% (cat.name, cat.name, affectionDown,cat.name,cat.affection))
        else:
            affectionUp = rd.randint(1,10)
            print('''%s가 당신이 지켜보는 시선에 편안함을 느낍니다. 당신이 지켜준다고 생각하고 있습니다.
            %s와의 친밀감이 %d만큼 올라갑니다.
            \n현재 %s와의 친밀감 %d''' %(cat.name, cat.name, affectionUp, cat.name, cat.affection))
        
    
    def actionWithCat(self,choNum,cat:Cat):
            
        if choNum == 1:
            self.feed()

        elif choNum == 2:
            self.touch(cat)
        
        elif choNum == 3:
            self.stare(cat)
        
        else:
            print('없는 행동입니다.')
    
    def meetCat(self,cat:Cat):
        
        print('%s가 어디있을까...잘못하면 못 만날 수도 있겠는데?' %cat.name)

        if cat.affection <= 33:
            catMeetProb = rd.randint(1,10)

            if catMeetProb >= 8:
                print('''\n%s을 만났다!\n
                1. 먹이주기
                2. 쓰다듬기
                3. 지켜보기\n''' % cat.name)

                actNum = int(input())

                while True:
                    try:
                        self.actionWithCat(actNum,cat)

                        break

                    except Exception:
                    
                        print('\n없는 행동입니다. 다시 선택해주세요\n')
            else: 
                print('오늘은 %s를 만날 수 없었습니다... 다음엔 꼭 만날 수 있기를!' % cat.name)
                cat.affectionDown()

        elif cat.affection >33 and cat.affection <= 67:
            catMeetProb = rd.randint(1,10)

            if catMeetProb >= 5:
                print('''\n%s을 만났다!\n
                1. 먹이주기
                2. 쓰다듬기
                3. 지켜보기\n''' % cat.name)

                actNum = int(input())

                while True:
                    try:
                        self.actionWithCat(actNum,cat)

                        break

                    except Exception:
                    
                        print('\n없는 행동입니다. 다시 선택해주세요\n')
            else: 
                print('오늘은 %s를 만날 수 없었습니다... 다음엔 꼭 만날 수 있기를!' % cat.name)
                cat.affectionDown()
        
        else:
            
            catMeetProb = rd.randint(1,10)

            if catMeetProb >= 2:
                print('''\n%s을 만났다!\n
                1. 먹이주기
                2. 쓰다듬기
                3. 지켜보기\n''' % cat.name)

                actNum = int(input())

                while True:
                    try:
                        self.actionWithCat(actNum,cat)

                        break

                    except Exception:
                    
                        print('\n없는 행동입니다. 다시 선택해주세요\n')
            else: 
                print('오늘은 %s를 만날 수 없었습니다... 다음엔 꼭 만날 수 있기를!' % cat.name)
                cat.affectionDown()