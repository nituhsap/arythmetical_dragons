# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Healer(Helper):
    pass


class Drunk_Priest(Healer):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer
       
    def __init__(self):
        self._heal = 45
        
    def question(self):

        self._quest = 'Tell me, how many Suns can thou see in this heavenly sky?'
        self.set_answer(1)
