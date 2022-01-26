from ClassFood import Food
#고양이 클래스
#속성
#   체력    
#   포만감
#   친밀감
#   성별
#기능   
#   먹기
#   
class Cat:
    
    MAX_HEALTHPOINT = 100
    MAX_SATIETY = 100
    MAX_AFFECTION = 100
    
    def __init__(self,name,sex):
        self.name = name #고양이의 이름
        self.sex = sex #고양이의 성별, 나중에 중성화 할 때 self.sex = '중성'으로 바뀜.
        self.healthPoint = 30 #체력 : 포만감이 20미만이면 체력이 지속적으로 깎임. 0이 되면 게임 종료.
        self.satiety = 30 #포만감 : 음식을 통해 포만감이 채워짐.
        self.affection = 0
    
    def eat(self,food:Food):
        
        if self.satiety + food.satiety >= self.MAX_SATIETY:
            self.satiety = 100
        else:
            self.satiety = self.satiety + food.satiety
        
        if self.affection + food.affection >= self.MAX_AFFECTION:
            self.affection = 100
        else:
            self.affection = self.affection + food.affection
        
        if self.healthPoint + food.healthPoint>= self.MAX_HEALTHPOINT:
            self.healthPoint = 100
        else:
            self.healthPoint = self.healthPoint + food.healthPoint
        
        print("%s의 포만감은 %d, 친밀감은 %d, 체력은 %d입니다" %(self.name, self.satiety, self.affection,self.healthPoint))


