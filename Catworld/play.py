from ClassCat import *
from ClassCompany import Company
from ClassConvinienceStore import *
from ClassPlayer import *
from ClassFood import *
import random

store = ConvinienceStore('편의점')
company1 = Company('회사')
playername = input('당신의 이름을 입력해주세요 : ')
player = Player(playername) 
print('%s님! 고양이 월드에 오신 것을 환영합니다.' % playername)

while True:
    print("""
    1. 게임시작
    2. 불러오기
    3. 종료""")
    op = int(input("메뉴를 선택하세요 : "))
    if op == 1:
        
        print('당신은 집 앞을 지나가다 아기고양이가 야옹야옹 우는 소리를 들었습니다.')
        
        print('집에 데려가서 키우고 싶지만 여건이 안됩니다! 길고양이 키우기 시작!')
        
        print('우선 고양이의 이름을 정해주세요')
        
        catname = input('고양이의 이름을 정해주세요 : ')
        
        catsex = random.randint(1,2)
        if catsex == 1:
            catsex ='수컷'
        else: catsex ='암컷'    
        cat1 = Cat(catname,catsex)

        print('당신이 발견한 고양이의 이름은 %s 성별은 %s 입니다.' % (cat1.name, cat1.sex))
        print('당신은 하루마다 일을 해서 돈을 벌 수 있습니다.\n번 돈으로 고양이에게 매일 음식을 사다줘야 합니다.')
        print('고양이는 포만감, 친밀감, 체력을 갖고 있습니다.\n친밀감이 높을수록 고양이에게 할 수 있는 행동들이 많습니다.')
        print('또한 포만감이 높으면 고양이의 체력이 회복되지만 포만감이 낮으면 체력이 줄어듭니다.')
        print('당신이 기르는 고양이의 체력이 0이 되면 게임 종료입니다.')