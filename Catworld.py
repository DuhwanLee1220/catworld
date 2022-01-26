class Cat:
    satiety = 20  #포만감(0~100)
    cleanness = 20 #청결도(0~100)
    healthPoint = 50 #체력 - 청결도와 포만감이 일정 수준 
                     #이하로 떨어지면 체력이 줄어듦(0~100)
    affection = 0
    food =['참치캔','츄르','영양제']
    age = 0
    day = 1
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex
    def feed(self,food):
        if food == '참치캔':
            self.satiety = self.satiety + 7
            self.affection = self.affection + 3
        elif food == '츄르':
            self.satiety = self.satiety + 2
            self.affection = self.affection + 5
        elif food == '영양제':
            self.satiety += 1
            self.affection += 1
            self.healthPoint += 5
    def touch(self):
        self.affection += 10
N,S =map(str,input().split())
cat1 = Cat(N,S)        
userAction = input('수행할 동작을 입력하세요(먹이주기,쓰다듬기,TNR이 있습니다.) : ')
if userAction == '먹이주기':
    userAction2 = input("""'참치캔', '츄르', '영양제' 중에서 선택하세요 : """)
    if userAction2 == '참치캔':
        cat1.feed('참치캔')
        if cat1.healthPoint >=100:
            cat1.healthPoint == 100
        elif cat1.satiety >=100:
            cat1.satiety == 100
        elif cat1.affection >= 100:
            cat1.affection == 100
        print('웨옹..........챱챱챱챱(내가 사라지길 기다리다가 참치캔을 먹었다.)')
        print('%s의 포만감은 %d입니다.' % (cat1.name, cat1.satiety))
        print('%s와의 유대감은 %d입니다.' % (cat1.name, cat1.affection))
        print('%s의 체력은 %d입니다.' % (cat1.name, cat1.healthPoint))
    elif userAction2 == '츄르':
        if cat1.affection <= 30:
            print('내가 너무 낯선걸까... %s(이)가 도망가버렸다' % cat1.name)
        else:
            cat1.feed('츄르')
            print('츕츕 쯃쯃 츅츅ㅂ류츏츕 챫ㅌ챫챱챱챱......(내 손까지 핥아먹은 것 같다.)')
        if cat1.healthPoint >=100:
            cat1.healthPoint == 100
        elif cat1.satiety >=100:
            cat1.satiety == 100
        elif cat1.affection >= 100:
            cat1.affection == 100
        print('%s의 포만감은 %d입니다.' % (cat1.name, cat1.satiety))
        print('%s와의 유대감은 %d입니다.' % (cat1.name, cat1.affection))
        print('%s의 체력은 %d입니다.' % (cat1.name, cat1.healthPoint))    
    elif userAction2 == '영양제':
        cat1.feed('영양제')
        if cat1.healthPoint >=100:
            cat1.healthPoint == 100
        elif cat1.satiety >=100:
            cat1.satiety == 100
        elif cat1.affection >= 100:
            cat1.affection == 100
        else:
            pass
        print('%s의 포만감은 %d입니다.' % (cat1.name, cat1.satiety))
        print('%s와의 유대감은 %d입니다.' % (cat1.name, cat1.affection))
        print('%s의 체력은 %d입니다.' % (cat1.name, cat1.healthPoint))
    else:
        print("""'%s' 따위의 음식은 냥냥이월드에 존재하지 않다냥!!!!!\n보여드린 음식 중에서 선택해달라냥!!!!""" % userAction2)
elif userAction == '쓰다듬기':
    if cat1.affection <= 50:
        print('웨웽에에에에엙!!!크와아아아앙 하아ㅏ앍 하앍 하앍캬아아아아악!!!!\n.......\n%s(이)가 나를 할퀴고 깨물고 도망갔다...! 너무아파....' % cat1.name)
    else:
        cat1.touch()
        print('%s의 포만감은 %d입니다.' % (cat1.name, cat1.satiety))
        print('%s와의 유대감은 %d입니다.' % (cat1.name, cat1.affection))
        print('%s의 체력은 %d입니다.' % (cat1.name, cat1.healthPoint))
elif userAction =='TNR':
    if cat1.affection <= 30:
        print('캬아앍!!!!!!!!!!............어떻게 눈치채고 도망가버렸다..')
    cat1.sex = '중성'
else:
    print('그런 행동은 고양이 월드에 존재하지 않습니다.')