# coding: utf-8
# license: GPLv3
from enemies import *
from friends import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, entity_list):
    for entity in entity_list:
        if isinstance(entity, Drunk_Priest):
            print('Вышел', entity)
            print('Привет, я сегодня в очень хорошем настроении и готов помочь тебе, если ты ответишь на мой вопрос. ', entity.question())
            answer = annoying_input_int('Ответ:')

            if entity.check_answer(answer):
                print('Верно! \n**', entity, 'кастует какие-то заклинания, звучащие, как тарабаршина**')
                entity.heal(hero)
            else:
                print('Ты ошибся! \n** Или ты не хочешь быть вылеченным?! ... Что ж... Тогда прощай!**')

        else:
            print('Вышел', entity)
            while entity.is_alive() and hero.is_alive():
                print('Вопрос:', entity.question())
                answer = annoying_input_int('Ответ:')

                if entity.check_answer(answer):
                    hero.attack(entity)
                    print('Верно! \n**', entity, 'кричит от боли **')
                else:
                    entity.attack(hero)
                    print('Ошибка! \n** вам нанесён удар... **')
            if entity.is_alive():
                break
            print(entity, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        hero = Hero(input())

        dragon_number = 10
        dragon_list = generate_dragon_list(dragon_number)
        assert(len(dragon_list) == dragon_number)
        print('У Вас на пути', dragon_number, 'персонажей!')
        game_tournament(hero, dragon_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
