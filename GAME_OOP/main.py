from player import Player
from enemy import Enemy,Troll,Vampire,Vampireking
import random

zen = Player("Zen")
monster = Enemy("Basic", 24, 1)
print(monster)
monster.take_damage(12)
print(monster)

monster.take_damage(8)
print(monster)

monster.take_damage(4)
print(monster)

monster.take_damage(2)
print(monster)

print('><'*50)

ugly_troll = Troll("grr")
print("Here comes the Ugly - {} " .format(ugly_troll))

toll = Troll("Yuck")
print("Here comes another one - {} ".format(toll) )

ugly_troll.grunt()
toll.grunt()

# toll.take_damage(12)
# print(toll)

print('><'*50)

kuro = Vampire("kuro")
shiro = Vampire("shiro")

print(kuro)
print(shiro)
kuro.take_damage(134)
shiro.take_damage(24)
print(kuro)
print(shiro)

print('><'* 50)

while toll.alive:
    print(toll)
    toll.take_damage(random.randint(1,5))
    print(toll)

print('><'*50)

while kuro.alive:
    print(kuro)
    kuro.take_damage(1)
    print(kuro)

print('><' * 50)

shiki = Vampireking("shiki")
print(shiki)
shiki.take_damage(12)
print(shiki)


# print(zen.name)
# print(zen.lives)
# zen.lives -= 1
# print(zen)

# zen.lives -= 1
# print(zen)

# zen.lives -= 1
# print(zen)

# zen.lives -= 1
# print(zen)

# zen._set_level(5)
# print(zen)

# print(zen._get_level())

# zen.score = 200

# print(zen)