#!/usr/bin/env python
import prompt
import brain_games.scripts.module
from random import randint

#Описание правил игры
brain_games.scripts.module.describe_rules('Answer "yes" if given number is prime. Otherwise answer "no".')

#Счетчик
def counts():
    i = 1

    while i <= 3:

        RANDOM_NUMBER = randint(1, 100)

        #Задаем переменную correct_answer
        brain_games.scripts.module.correct_answer = ' '
            
        #Проверка на простое ли это число
        def сhecked_prime(n):
            def isPrime(n):
                d = 2
                while n % d != 0:          
                    d += 1
                return d == n

            if n == 1 or n == 2 or isPrime(n):
                return 'yes'
            return 'no'

        #Задаем значение переменной correct_answer
        brain_games.scripts.module.correct_answer = сhecked_prime(RANDOM_NUMBER)

        #Вопрос игроку
        brain_games.scripts.module.ask_question(RANDOM_NUMBER)
            
        #Поле для ввода ответа
        user_answer = input("Your answer: ")

        #Проверка правильности ответа
        brain_games.scripts.module.checked_user_answer(user_answer)
        
        i += 1
  
    brain_games.scripts.module.congratulate(brain_games.scripts.module.name)


def main():
    counts()


if __name__ == '__main__':
    main()