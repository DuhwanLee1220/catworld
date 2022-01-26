from msilib.schema import Error
from ClassPlayer import Player
import random as rd
import time
#일터
#일터에서 문제를 내고 문제를 풀면 player는 돈을 받음
#1번 문제유형: 몫 예측하기
#2번 문제유형: 평균 구하기(나머지 X)
#3번 문제유형: 무작위로 나오는 수 맞히기
#4번 문제유형: 번호판 4자리 수 더하기
class Company:
    
    def __init__(self,name):
        self.name = name
    
    def problem(self):
        
        questionNum = rd.randint(1,4)
        
        print('%d번 문제 유형입니다.' % questionNum)
        if questionNum == 1:
            a = rd.randint(1,601)
            b = rd.randint(600,1201)
            print('%d를 %d로 나눈 값의 몫을 입력하시오.' %(b,a))
            
            k = 5
            for l in range(0,6):
                print(k - l)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            
            takeTime = end - start
            
            print('걸린시간 :',takeTime)
            
            if takeTime > 5:
                print('5초를 초과했습니다.')
                answer = 1300 #600~1200까지의 숫자를 1~600으로 나눈 결과 중 1300은 절대 몫이 될 수 없음.
            else: pass
            
            if answer != b // a:
                print('틀렸습니다')
                problemResult = False
            else:
                print('정답입니다!')
                problemResult = True
        elif questionNum == 2:
            print('1~45까지의 무작위의 숫자가 2~10개만큼 무작위로 주어집니다.\n당신은 이 무작위의 숫자의 평균을 구하면 됩니다.\n단 나머지는 구할 필요 없습니다.')
            avgList = []
            randomrange = rd.randint(3,10)
            for i in range(1,randomrange):
                avgList.append(rd.randint(1,45))
            print(avgList)
            
            result = 0
            for j in avgList:
                result += j
            
            k = 5
            for l in range(0,6):
                print(k - l)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            takeTime = end - start
            print('걸린시간 :',takeTime)
            if takeTime > 5:
                print('5초를 초과했습니다.')
                answer = 0 #1~45까지의 숫자 2~10개 중 0은 절대 평균이 될 수 없음
            else: pass

            if answer != result // len(avgList):
                print('틀렸습니다')
                problemResult = False
            else:
                print('정답입니다!')
                problemResult = True
        
        elif questionNum == 3:
            randnumber = rd.randrange(1,11)
            print('아쉽게도 가장 고난이도의 문제를 풀게 되었습니다.\n1~10까지 무작위로 나오는 수를 맞히면 됩니다.')
            
            i = 5
            for j in range(0,6):
                print(i - j)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            takeTime = end - start
            print('걸린시간 :',takeTime)
            if takeTime > 5:
                print('5초를 초과했습니다.')
                answer = 11 #1~10까지의 숫자중에서 11은 절대 정답이 될 수 없음.
            else: pass

            if randnumber != answer:
                print('틀렸습니다.')
                problemResult = False
            else:
                print('정답입니다!')
                problemResult = True

        elif questionNum == 4:
            stNum = rd.randrange(0,10)
            ndNum = rd.randrange(0,10)
            rdNum = rd.randrange(0,10)
            thNum = rd.randrange(0,10)
            
            print('%d%d%d%d의 자동차 번호판이 있습니다. 이 수를 모두 곱하세요' %(stNum,ndNum,rdNum,thNum))
        
            i = 5
            for j in range(0,6):
                print(i - j)
                time.sleep(1)
            start = time.time()
            answer = int(input('5초 안에 값을 입력하세요: '))
            end = time.time()
            takeTime = end - start
            print('걸린시간 :',takeTime)
            if takeTime >= 5:
                answer = 9**5 #9의 5제곱은 4자릿수 번호판에서 절대 정답이 될 수 없음.
            else: pass
            
            if answer != stNum * ndNum * rdNum * thNum:
                print('틀렸습니다')
                problemResult = False
            else:
                print('정답입니다!')
                problemResult = True
        
        else: pass

        if problemResult == True:
            Player.addMoney(10)
            print('잔고는 %d 입니다.'%Player.balance)
        else:
            Player.addMoney(1)
            print('잔고는 %d 입니다.'%Player.balance)