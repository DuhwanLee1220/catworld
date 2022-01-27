from re import L
from ClassCat import *
from ClassCompany import Company
from ClassConvinienceStore import *
from ClassPlayer import *
from ClassFood import *
import random as rd
from printer import *
import sys
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
printInfo('%s님! 고양이 월드에 오신 것을 환영합니다.' % playername)

    

while True:
    printMenu("""
    1. 게임시작
    2. 불러오기
    3. 종료""")

    op = int(input("메뉴를 선택하세요 : "))

    if op == 1:

        printLineFeed1('당신은 집 앞을 지나가다 아기고양이가 야옹야옹 우는 소리를 들었습니다.')
        printLaterFewSec(2)
        printLineFeed1('집에 데려가서 키우고 싶지만 안됩니다. 길고양이 키우기를 시작합니다!')
        printLaterFewSec(2)
        printLineFeed1('우선 고양이의 이름을 정해주세요!')

        catname = input('고양이의 이름을 정해주세요 : ')

        catsex = rd.randint(1,2)
        if catsex == 1:
            catsex ='수컷'
        else: catsex ='암컷'    
        cat1 = Cat(catname,catsex)
        
        printLineFeed1('당신이 발견한 고양이의 이름은 %s 성별은 %s 입니다.' % (cat1.name, cat1.sex))
        printLaterFewSec(2)
        printLineFeed1('당신은 하루마다 일을 해서 돈을 벌 수 있습니다.\n번 돈으로 고양이에게 매일 음식을 사다줘야 합니다.')
        printLaterFewSec(2)
        printLineFeed1('고양이는 포만감, 친밀감, 체력을 갖고 있습니다.\n친밀감이 높을수록 고양이에게 할 수 있는 행동들이 많습니다.')
        printLaterFewSec(2)
        printLineFeed1('또한 포만감이 높으면 고양이의 체력이 회복되지만 포만감이 낮으면 체력이 줄어듭니다.')
        printLaterFewSec(2)
        printLineFeed1('당신이 기르는 고양이의 체력이 0이 되면 게임 종료입니다.')
        
        break

    elif op == 2:
        printWarning('그런 기능 없습니다')
        sys.exit()
        
    elif op == 3:
        printWarning('종료합니다.')
        sys.exit()
        
    else: 
        printWarning('잘못된 입력')
        
        pass

def firstDay():
    printMenu('''
    회사에서 일을 마치고 집으로 오는 어느날...
    집 앞 주차장에서 이상한 소리가 들린다.
    ''')
    printLaterFewSec(2)
    printLineFeed1('..........미야옹....미야오옹...')

    printMenu('''
    1.가본다
    2.무시한다
    ''')

    choiceOne = int(input('입력해주세요: '))

    if choiceOne == 1:
        printLineFeed1('''
        '야옹~ 야옹~' 어디선가 고양이 소리가 들린다!
        가까이 다가가봤더니 아기고양이가 야옹야옹 울고있다.
        엄마고양이는 보이지 않는다...
        ''')
        
        printMenu('''
        1.기다린다
        2.무시한다
        ''')
        choiceTwo = int(input('입력해주세요: '))

        if choiceTwo == 1:
            printLaterFewSec(2)
            printLineFeed2('''
            엄마고양이는 보이지 않고 집에 데려갈 수도 없다...
            일단 밥을 줘야겠다.''')

        else:
            printLineFeed2('''
            아기고양이는 알아서 잘 살겁니다...
            당장 먹을 것이 없어도 이것이 스트릿의 생존법칙이죠.
            게임이 끝났습니다.''')    
            sys.exit()
    else:
        printLineFeed2('''
        나쁜사람....
        게임이 끝났습니다.
        ''')
        sys.exit()
    
    printLaterFewSec(2)
    
    printMenu('''
    당신은 지금부터 당신의 %s에게 매일 먹이를 줄 수 있습니다.

    먹이의 종류는 참치캔,츄르,영양제,물,사료 5가지가 있습니다.

    이 먹이는 회사에서 일을 해서 번 돈으로 편의점에 가서 구입하실 수 있습니다.

    집사의 하루 일과는 정해져있습니다. 우선 당신의 인벤토리에 참치캔 1개를 넣어놨습니다.

    %s에게 어서 참치캔 1개를 먹여주세요!
    ''' %(cat1.name,cat1.name))

    player.addInventory(food1)
    
    player.feed(cat1)

    print('이렇게 당신이 먹이를 줄 때마다 %s의 포만감과 친밀감 체력이 나타나게 됩니다.' %cat1.name)
    print('고양이와의 친밀감을 높이고 %s를 집고양이로 만드세요!' % cat1.name)

firstDay()

actionCount = 0

while True:
    
    if cat1.healthPoint <= 0:
        printWarning("""
        당신은 %s를 제대로 돌보지 않았습니다. 당신의 무책임함이 %s가 당신을 떠나게 만들었습니다.
        이제 %s는 더 이상 이 세상에서 볼 수 없습니다. 당신이 제대로 돌보지 않는 동안
        %s는 길거리에서 차에 치였을 수도, 다른 동물에게 잡아먹혔을 수도 있습니다.
        어쨌든 확실한건 %s의 방치로 인해 %s는 더 이상 이 세상에 존재하지 않는다는 것입니다.
        

        게임을 종료합니다.
        """ % (cat1.name,cat1.name,cat1.name,cat1.name,player.name,cat1.name))
        sys.exit()
    else:
        
        if cat1.affection >= cat1.MAX_AFFECTION:
            printWind("""
            고생하셨습니다. 당신의 꾸준한 관심과 사랑 덕분에
            %s가 결국 당신에게 마음을 열고 다가갑니다.
            %s는 당신에게 의지하고 함께하기를 원합니다.
            %s를 입양하시겠습니까?

            1.네

            2.아니오    
            """)
            answertoQ = int(input('입력해주세요: '))
            printLaterFewSec(5)

            while True:
                if answertoQ == 1:
                    printMenu('이제 %s와 당신은 영원히 함께입니다! %s는 집고양이가 되어 Catworld에서 영원히 당신과 함께할 것입니다.\n\n\n 게임을 종료합니다.' % (cat1.name,cat1.name))
                    sys.exit()

                elif answertoQ == 2:
                    printMenu('''
                    고양이를 키울 여건이 되지 않고 자신이 없다면 입양을 포기하는 것 또한 방법입니다.
                    당신은 오히려 책임감이 있는사람입니다. 자신의 한계를 정확히 아는 것은
                    오히려 한 생명을 가볍게 대하는 것이 아닌 진실되게 생각하고 있다는 것입니다.
                    %s는 당신의 사랑과 관심을 등에 업고 Catworld 스트릿의 최강자가 될 것입니다.
                    '''% cat1.name)

                    sys.exit()
                else:
                    printWarning('잘못된 선택입니다. 다시 선택해주세요')
        else:
            pass

        #####################
        # 포만감에 따라 체력이 늘어나고 줄어듦. -> 나중에 cat클래스에 추가하여 코드 길이 짧게 할 것.
        if cat1.satiety < 30:
            cat1.healthPoint -= 3
        elif cat1.satiety>=30 and cat1.satiety <60:
            pass
        else:
            cat1.healthPoint += 3
        #####################
                
        if actionCount == 3:
            randSatietyDown = rd.randint(1,5)
            
            cat1.satiety -= randSatietyDown
            printLaterFewSec(2)
            printLineFeed1('자연적으로 %s의 포만감이 %d만큼 줄어들었습니다.\n현재 포만감은 %d입니다.' % (cat1.name,randSatietyDown,cat1.satiety))
            printLaterFewSec(2)
            print('하루에 할 수 있는 동작을 전부 수행하셨습니다.')
            printLaterFewSec(2)
            print('다음날로 넘어갑니다.')
            printLaterFewSec(2)
            dayInGame += 1
            actionCount = 0
        else:
            while True:
                print('\n%d번째 날의 %d번째 행동입니다.\n' % (dayInGame,actionCount+1))
                printLaterFewSec(1)
                print('''
                1. 회사 가기
                2. 편의점 가기
                3. %s만나러 가기
                4. 행동 1개 쉬기
                5. 내 정보 확인
                6. %s의 정보 확인
                7. 저장하기(기능 미구현)
                5번, 6번, 7번의 행동은 행동횟수에 포함되지 않습니다.
                '''% (cat1.name, cat1.name))
                playerAction = int(input('수행할 동작을 입력해주세요 : '))

                try:
                    if playerAction == 1:

                        company1.problem(player)

                        actionCount += 1
                        break

                    elif playerAction == 2:

                        store.printSellList()

                        while True:

                            try:

                                whatbuy = int(input('\n\n사고싶은 물건의 번호를 입력하세요 : '))

                                foodbuy = store.sellList[whatbuy-1]

                                if food1.name == foodbuy:
                                    store.buyFood(food1,player)
                                    printLaterFewSec(2)
                                    printLineFeed1('추가 구매를 원하시면 1을 아니면 아무 키나 눌러주세요.')
                                    buyMore = input()
                                    try:
                                        if buyMore == '1':
                                            pass
                                        else:
                                            break
                                    except Exception:
                                        print('다음번엔 엔터 누르지 마세요')
                                        break
                                    

                                elif food2.name == foodbuy:
                                    store.buyFood(food2,player)
                                    printLaterFewSec(2)
                                    printLineFeed1('추가 구매를 원하시면 1을 아니면 아무 키나 눌러주세요.')
                                    buyMore = input()
                                    try:
                                        if buyMore == '1':
                                            pass
                                        else:
                                            break
                                    except Exception:
                                        print('다음번엔 엔터 누르지 마세요')
                                        break

                                elif food3.name == foodbuy:
                                    store.buyFood(food3,player)
                                    printLaterFewSec(2)
                                    printLineFeed1('추가 구매를 원하시면 1을 아니면 아무 키나 눌러주세요.')
                                    buyMore = input()
                                    try:
                                        if buyMore == '1':
                                            pass
                                        else:
                                            break
                                    except Exception:
                                        print('다음번엔 엔터 누르지 마세요')
                                        break

                                elif food4.name == foodbuy:
                                    store.buyFood(food4,player)
                                    printLaterFewSec(2)
                                    printLineFeed1('추가 구매를 원하시면 1을 아니면 아무 키나 눌러주세요.')
                                    buyMore = input()
                                    try:
                                        if buyMore == '1':
                                            pass
                                        else:
                                            break
                                    except Exception:
                                        print('다음번엔 엔터 누르지 마세요')
                                        break

                                elif food5.name == foodbuy:
                                    store.buyFood(food5,player)
                                    printLaterFewSec(2)
                                    printLineFeed1('추가 구매를 원하시면 1을 아니면 아무 키나 눌러주세요.')
                                    buyMore = input()
                                    try:
                                        if buyMore == '1':
                                            pass
                                        else:
                                            break
                                    except Exception:
                                        print('다음번엔 엔터 누르지 마세요')
                                        break

                                else:
                                    pass

                                
                            except Exception:
                                print('\n없는 상품입니다.\n')
                                printLineFeed1('뒤로가기를 원하시면 1을 입력해주세요.\n아니면 아무 키나 눌러주세요')
                                wantBack = int(input('입력해주세요: '))
                                if wantBack == 1:                                
                                    actionCount -=1
                                    break
                                else:
                                    pass

                        

                        actionCount += 1
                        break

                    elif playerAction == 3:

                        player.meetCat(cat1)

                        actionCount += 1

                        break

                    elif playerAction == 4:

                        cat1.affection -= 2

                        cat1.satiety -= 2

                        if cat1.affection < cat1.MIN_AFFECTION:
                            cat1.affection = 0
                        else:
                            pass
                        if cat1.satiety < cat1.MIN_AFFECTION:
                            cat1.satiety = 0
                        else:
                            pass
                        printInfo('''
                        쉬는동안 %s와의 친밀감,포만감이 2만큼 내려갔습니다.
                        ''' % (cat1.name))
                        printLineFeed2('%s와의 친밀감 %d, %s의 포만감 %d' % (cat1.name,cat1.affection,cat1.name,cat1.satiety))

                        printLaterFewSec(2)
                        printInfo('''
                        휴식을 취한 대신 당신은 음식과 돈을 선택해서 받을 수 있습니다.
                        무엇을 받으시겠습니까?
                        1.음식(5가지 종류 중 랜덤)
                        2.돈(1~5원, 랜덤)
                        ''')

                        choiceForM = int(input('입력해주세요: '))
                        if choiceForM == 1:
                            randFood = rd.randint(1,5)
                            player.addInventoryNum(randFood)
                        else:
                            randMoney = rd.randint(1,5)
                            player.balance += randMoney
                            printInfo('당신의 잔고입니다. %d만큼 증가하여 %d입니다.' % (randMoney, player.balance) )

                        actionCount += 1
                        break
                    elif playerAction == 5:
                        print('''
                        이름: %s
                        잔고 : %s
                        소지품 : %s
                        ''' % (player.name, player.balance, player.playerInventory))

                    elif playerAction == 6:
                        print('''
                        고양이 이름: %s
                        친밀감: %s
                        포만감: %s
                        체력: %s
                        ''' %(cat1.name,cat1.affection,cat1.satiety,cat1.healthPoint))
                    
                    elif playerAction == 7:
                        f = open('C:\\Users\\PC\\Documents\\catworld\\savefile.txt','w')
                        f.write('파일을 저장합니다.')
                        f.close()

                except Exception:
                    print('없는 동작입니다.')