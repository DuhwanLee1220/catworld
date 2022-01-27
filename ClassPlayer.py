from ClassFood import *
from ClassCat import *
import random as rd
from printer import *

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
        if self.balance - money < 0:
            printInfo("돈이 부족합니다!")
        else:
            self.balance = self.balance - money
            printInfo('%d만큼의 돈이 빠져나가고\n잔고가 %d만큼 남아있습니다' % (money,self.balance))

    def addInventory(self, food:Food):
        
        self.playerInventory.append(food.name)
        
        printInfo('인벤토리에 %s이(가) 추가되었습니다!' % food.name)
        print('당신의 인벤토리입니다.')
        printInfo(self.playerInventory)

    def addInventoryNum(self,rdnum):
        
        if rdnum == food1.foodNum:
            self.addInventory(food1)

        elif rdnum == food2.foodNum:
            self.addInventory(food2)

        elif rdnum == food3.foodNum:
            self.addInventory(food3)

        elif rdnum == food4.foodNum:
            self.addInventory(food4)

        elif rdnum == food5.foodNum:
            self.addInventory(food5)

    def showInventory(self):
       inventoryList = list(self.playerInventory)
       if len(self.playerInventory) == 0:
           print('아무것도 소지하고 있지 않습니다.')
       
       else: 
           print(inventoryList)   

    def feed(self,cat:Cat):
        
        self.showInventory()
        
        if len(self.playerInventory) == 0:
            printInfo('인벤토리에 아무것도 없기 때문에 음식을 줄 수 없습니다.')
        
        else:    
            while True:
                self.whatIHave = input('어떤 음식을 주겠습니까? : ')

                if self.whatIHave not in self.playerInventory:
                    printInfo('''"%s"을(를) 소지하고 있지 않습니다.''' % self.whatIHave)

                else:
                    self.playerInventory.remove(self.whatIHave)
                    printInfo('%s을(를) 주었습니다.' % self.whatIHave)
                    if self.whatIHave == food1.name:
                        cat.eat(food1)
                    elif self.whatIHave == food2.name:
                        cat.eat(food2)
                    elif self.whatIHave == food3.name:
                        cat.eat(food3)
                    elif self.whatIHave == food4.name:
                        cat.eat(food4)
                    elif self.whatIHave == food5.name:
                        cat.eat(food5)
                    break
    def touch(self,cat : Cat):
        
        if cat.affection <= 50:
            printWarning('%s와 친밀감이 너무 낮아 쓰다듬을 수 없습니다' % cat.name)
            printLaterFewSec(3)
            printWarning('%s가 당신을 공격했습니다!!!!!!!!!!' %cat.name)
            affectionDown = rd.randint(1,5)
            cat.affection -= affectionDown
            printInfo('%s와의 친밀감이 %d 만큼 하락하여 %d만큼의 친밀감을 갖고 있습니다.' %(cat.name, affectionDown, cat.affection))
        
        else:
            printWind('%s가 고로롱 소리를 내며 편안함을 느낍니다.' % cat.name)
            affectionUp = rd.randint(1,5)
            cat.affection += affectionUp
            printInfo('%s와의 친밀감이 %d 만큼 상승하여 %d만큼의 친밀감을 갖고 있습니다.' %(cat.name, affectionUp, cat.affection))

    def stare(self,cat:Cat):
        
        printLineFeed2('%s를 지켜보고 있습니다...' %(cat.name))
        if cat.affection <= 40:
            affectionDown = rd.randint(1,5)
            printLaterFewSec(3)
            printWarning('%s가 시비를 거는거로 오해했습니다!\n%s와의 친밀감이 %d만큼 차감됩니다.\n현재 %s와의 친밀감 %d'% (cat.name, cat.name, affectionDown,cat.name,cat.affection))
        else:
            affectionUp = rd.randint(1,5)
            printLaterFewSec(3)
            printWind('''
            %s가 당신이 지켜보는 시선에 편안함을 느낍니다. 당신이 지켜준다고 생각하고 있습니다.
            %s와의 친밀감이 %d만큼 올라갑니다.
            \n현재 %s와의 친밀감 %d
            ''' %(cat.name, cat.name, affectionUp, cat.name, cat.affection))
        
    
    def actionWithCat(self,choNum,cat:Cat):
            
        if choNum == 1:
            if len(self.playerInventory) == 0:
                printLineFeed2('''
                아무것도 소지하고 있지 않습니다.
                %s가 실망하며 돌아갔습니다.
                '''% cat.name )
                cat.satiety -= 3
                cat.affection -= 3
                printLaterFewSec(3)
                printInfo('''
                %s와의 친밀도가 3만큼 내려갔습니다.
                %s의 포만감이 3만큼 내려갔습니다.
                현재 %s와의 친밀도는 %d, 포만감은 %d입니다.
                ''' %(cat.name,cat.name,cat.name,cat.affection,cat.satiety))       
            else:
                self.feed(cat)
                

        elif choNum == 2:
            self.touch(cat)
        
        elif choNum == 3:
            self.stare(cat)
        
        else:
            printWarning('없는 행동입니다.')
    
    def meetCat(self,cat:Cat):
        
        printLineFeed2('%s가 어디있을까...잘못하면 못 만날 수도 있겠는데?' %cat.name)
        printLaterFewSec(3)

        if cat.affection <= 33:
            catMeetProb = rd.randint(1,100)

            if catMeetProb >= 70:
                printMenu('''
                %s을 만났다!

                1. 먹이주기
                2. 쓰다듬기
                3. 지켜보기\n''' % cat.name)

                actNum = int(input())

                while True:
                    try:
                        self.actionWithCat(actNum,cat)

                        break

                    except Exception:
                    
                        printWarning('없는 행동입니다. 다시 선택해주세요')
                        
            else: 
                printInfo('오늘은 %s이를 만날 수 없었습니다... 다음엔 꼭 만날 수 있기를!' % cat.name)
                printLaterFewSec(2)
                printLineFeed2('%s이와 만나지 못해 친밀도가 내려갑니다...' % cat.name)
                cat.affectionDown()
                printLaterFewSec(1)
                printLineFeed2('''
                %s와의 친밀도 %d '''%(cat.name, cat.affection))

        elif cat.affection >33 and cat.affection <= 67:
            catMeetProb = rd.randint(1,100)

            if catMeetProb >= 50:
                printMenu('''\n%s을 만났다!\n
                1. 먹이주기
                2. 쓰다듬기
                3. 지켜보기\n''' % cat.name)

                actNum = int(input())

                while True:
                    try:
                        self.actionWithCat(actNum,cat)

                        break

                    except Exception:
                    
                        printWarning('\n없는 행동입니다. 다시 선택해주세요\n')
            else: 
                printInfo('오늘은 %s를 만날 수 없었습니다... 다음엔 꼭 만날 수 있기를!' % cat.name)
                printLaterFewSec(2)
                printLineFeed2('%s와 만나지 못해 친밀도가 내려갑니다...' % cat.name)
                cat.affectionDown()
                printLaterFewSec(1)
                printLineFeed2('''
                %s와의 친밀도 %d
                '''%(cat.name, cat.affection))

        
        else:
            
            catMeetProb = rd.randint(1,100)

            if catMeetProb >= 20:
                printMenu('''\n%s을 만났다!\n
                1. 먹이주기
                2. 쓰다듬기
                3. 지켜보기\n''' % cat.name)

                actNum = int(input())

                while True:
                    try:
                        self.actionWithCat(actNum,cat)

                        break

                    except Exception:
                    
                        printWarning('\n없는 행동입니다. 다시 선택해주세요\n')
            else: 
                printInfo('오늘은 %s를 만날 수 없었습니다... 다음엔 꼭 만날 수 있기를!' % cat.name)
                printLaterFewSec(2)
                printLineFeed2('%s와 만나지 못해 친밀도가 내려갑니다...' % cat.name)
                cat.affectionDown()
                printLaterFewSec(1)
                printLineFeed2('''
                %s와의 친밀도 %d
                '''%(cat.name, cat.affection))

