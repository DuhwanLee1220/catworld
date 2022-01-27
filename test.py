from ClassCat import *
from ClassCompany import Company
from ClassConvinienceStore import *
from ClassPlayer import *
from ClassFood import *
import random as rd
from printer import *
import sys
player = Player('dd')
choiceForM = int(input('입력해주세요: '))

if choiceForM == 1:
    randFood = rd.randint(1,5)
    player.addInventoryNum(randFood)
    player.showInventory()
    
    a = input()
