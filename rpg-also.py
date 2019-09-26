# 2 classes
#     Hero
#         Attributes
#             Health
#             Power
#         Methods
#             Attack
#             Flee
#             Pass

#     Goblin
#         Attributes
#             Health
#             Power
#         Methods
#             Attack
#             Flee
#             Pass

# 3 classes
#     Hero
#     Goblin
#     Participent
#         Health
#         Power



class Hero:
    def __init__(self, power, health):
        self.power = power
        self.health = health

class Goblin:
    def __init__(self, power, health):
        self.power = power
        self.health = health

beowulf = Hero(10 , 10)
murky = Goblin(6, 2)
