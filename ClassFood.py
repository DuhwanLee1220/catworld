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

        
food1 = Food('참치캔',7,3,2,5)
food2 = Food('츄르',3,8,1,3)
food3 = Food('영양제',2,2,10,6)
food4 = Food('사료',5,3,4,5)
food5 = Food('물',3,2,5,2)

