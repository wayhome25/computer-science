from player import Player
from monster import *

play = Player()
ice = IceMonster()
fire = FireMonster()

print(ice)
print(fire)

monsters = []
monsters.append(ice)
monsters.append(fire)

# 다형성 코드: 코드는 같지만 결과는 다르다
for monster in monsters:
    play.attack(monster,'ICE')
    
for monster in monsters:
    print(monster)