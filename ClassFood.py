# 음식 : 고양이가 먹을 수 있는 음식으로 포만감과 애정, HP를 올려줌.
#   포만감
#   애정
#   HP
#종류는 참치캔, 츄르, 영양제, 사료
#
class Food:
    def __init__(self,name,satiety,affection,healthPoint,price):
        self.name = name
        self.satiety = satiety
        self.affection = affection
        self.healthPoint = healthPoint
        self.price = price
        
food1 = Food('참치캔',4,2,1,5)
food2 = Food('츄르',1,4,0,3)
food3 = Food('영양제',1,1,5,5)
food4 = Food('사료',3,2,2,5)
food5 = Food('물',1,1,2,2)
