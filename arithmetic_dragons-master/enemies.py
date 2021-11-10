# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    def __init__(self):
        self._color = None
        self._type = None

    def __repr__(self):
        return self._type + ' ' + self._color


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list
def generate_magicians_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def __init__(self):
        self._health = None
        self._attack = None
        self._color = None
        self._type = 'дракончик'
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'
        

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest
class RedDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._health = 150
        self._attack = 20
        self._color = 'красный'
    def question(self):
        x = randint(50,200)
        y = randint(1,50)
        self._quest = str(x) + '-' + str(y)
        self.set_answer(x-y)
        return self._quest
class BlackDragon(Dragon):
    def __init__(self):
        super().__init__()
        self._health = 250
        self._attack = 50
        self._color = 'чёрный'

    def question(self):
        x = randint(1,30)
        y = randint(1,30)
        self._quest = str(x) + '*' + str(y)
        self.set_answer(x*y)
        return self._quest

class Magicians(Enemy):
    def __init__(self):
        self._health = None
        self._attack = None
        self._color = None
        self._type = 'маг в шляпе'
    def set_answer(self, answer):
        self.__answer = answer
    def check_answer(self, answer):
        return answer == self.__answer

class CrazyWitch(Magicians):
    def __init__(self):
        super().__init__()
        self._health = 10
        self._attack = 1
        self._color = 'серо-буро-малинового цвета'
    def question(self):
        x = randint(1,10)
        self._quest = 'угадай число от 1 до 10'
        self.set_answer(x)
        return self._quest

class CrazyFairy(Magicians):
    def __init__(self):
        super().__init__()
        self._health = 10   
        self._attack = -1
        self._color = 'радужного цвета'
    def question(self):
        x = randint(1,10)
        self._quest = 'угадай число 1 до 10'
        self.set_answer(x)
        return self._quest

class CunningWizard(Magicians):
    def __init__(self):     
        super().__init__()
        self._health = 300
        self._attack = 25
        self._color = 'невидимка'           
    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self._quest = 'Остаток от деления ' + str(x) + ' на ' + str(y)
        self.set_answer(x%y)
        return self._quest







#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит анию, а чёрный -- умножению.


enemy_types = [GreenDragon, RedDragon, BlackDragon, CrazyWitch, CrazyFairy, CunningWizard]
