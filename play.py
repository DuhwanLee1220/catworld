from ClassCat import *
from ClassCompany import Company
from ClassConvinienceStore import *
from ClassPlayer import *
from ClassFood import *
import random as rd
dayInGame = 2
store = ConvinienceStore('편의점')

store.addItem(food1)
store.addItem(food2)
store.addItem(food3)
store.addItem(food4)
store.addItem(food5)

company1 = Company('회사')
playername =  input('당신의 이름을 입력해주세요 : ')
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

        catsex = rd.randint(1,2)
        if catsex == 1:
            catsex ='수컷'
        else: catsex ='암컷'    
        cat1 = Cat(catname,catsex)
        
        print('\n당신이 발견한 고양이의 이름은 %s 성별은 %s 입니다.' % (cat1.name, cat1.sex))
        print('\n당신은 하루마다 일을 해서 돈을 벌 수 있습니다.\n번 돈으로 고양이에게 매일 음식을 사다줘야 합니다.')
        print('\n고양이는 포만감, 친밀감, 체력을 갖고 있습니다.\n친밀감이 높을수록 고양이에게 할 수 있는 행동들이 많습니다.')
        print('\n또한 포만감이 높으면 고양이의 체력이 회복되지만 포만감이 낮으면 체력이 줄어듭니다.')
        print('\n당신이 기르는 고양이의 체력이 0이 되면 게임 종료입니다.')
        
        break

    elif op == 2:
        print('그런 기능 없습니다')
        break
    elif op == 3:
        print('종료합니다.')
        break
    else: 
        print('잘못된 입력')
        pass

def firstDay():
    print('''\n회사에서 일을 마치고 집으로 오는 어느날...
    집 앞 주차장에서 이상한 소리가 들린다.
    ''')

    choiceOne = int(input('1.가본다\n2.무시한다: '))

    if choiceOne == 1:
        print(''' '야옹~ 야옹~' 어디선가 고양이 소리가 들린다!
        가까이 다가가봤더니 아기고양이가 야옹야옹 울고있다.
        엄마고양이는 보이지 않는다...''')
        
        choiceTwo = int(input('1.기다린다\n2.무시한다: '))

        if choiceTwo == 1:
            print('''엄마고양이는 보이지 않고 집에 데려갈 수도 없다...
            일단 밥을 줘야겠다.''')

        else:
            print('''\n아기고양이는 알아서 잘 살겁니다...
            당장 먹을 것이 없어도 이것이 스트릿의 생존법칙이죠.
            \n게임이 끝났습니다.''')    
    else:
        print('\n나쁜사람....\n\n게임이 끝났습니다.')
    
    print('''\n\n당신은 지금부터 당신의 %s에게 매일 먹이를 줄 수 있습니다.
    먹이의 종류는 참치캔,츄르,영양제,물,사료 5가지가 있습니다.
    이 먹이는 회사에서 일을 해서 번 돈으로 편의점에 가서 구입하실 수 있습니다.
    집사의 하루 일과는 정해져있습니다. 우선 당신의 인벤토리에 참치캔 1개를 넣어놨습니다.
    %s에게 어서 참치캔 1개를 먹여주세요!\n\n''' %(cat1.name,cat1.name))
    player.addInventory(food1)
    player.feed()
    cat1.eat(food1)
    print('이렇게 당신이 먹이를 줄 때마다 %s의 포만감과 친밀감 체력이 나타나게 됩니다.' %cat1.name)
    print('아직 당신은 고양이와의 친밀감이 낮기 때문에 하루에 1가지의 상호작용밖에 수행할 수 없습니다.')

firstDay()

actionCount = 0

while True:
    if actionCount == 3:
        print('하루에 할 수 있는 동작을 전부 수행하셨습니다.')
        print('다음날로 넘어갑니다.')
        dayInGame += 1
        actionCount = 0
    else:
        print('\n%d번째 날입니다.\n' % dayInGame)
        print('''1. 회사 가기
        2. 편의점 가기
        3. %s만나러 가기
        4. 오늘 하루 쉬기
        5. 내 정보 확인
        6. %s의 정보 확인'''% (cat1.name, cat1.name))

    

        playerAction = int(input('수행할 동작을 입력해주세요 : '))
        try:
            if playerAction == 1:

                company1.problem(player)

                actionCount += 1

            elif playerAction == 2:

                store.printSellList()
                
                while True:

                    try:

                        whatbuy = int(input('\n\n사고싶은 물건의 번호를 입력하세요 : \n\n'))
                        foodbuy = store.sellList[whatbuy-1]
                        break
                    except Exception:
                        print('\n없는 상품입니다.\n')
                
                if food1.name == foodbuy:
                    store.buyFood(food1,player)

                elif food2.name == foodbuy:
                    store.buyFood(food2,player)

                elif food3.name == foodbuy:
                    store.buyFood(food3,player)

                elif food4.name == foodbuy:
                    store.buyFood(food4,player)

                elif food5.name == foodbuy:
                    store.buyFood(food5,player)    
                                
                actionCount += 1

            elif playerAction == 3:

                player.meetCat(cat1)

                actionCount += 1

            elif playerAction == 4:

                cat1.affectionDown
                cat1.satiety -= 10
                cat1.healthPoint -= 3

            elif playerAction == 5:
                print('''이름: %s
                잔고 : %s
                소지품 : %s''' % (player.name, player.balance, player.playerInventory))
            
            elif playerAction == 6:
                print('''고양이 이름: %s
                친밀감: %s
                포만감: %s
                체력: %s''' %(cat1.name,cat1.affection,cat1.satiety,cat1.healthPoint))
                
        except Exception:
            print('없는 동작입니다.')