#!/usr/bin/env python
import brain_games.scripts.module
from random import randint
from math import gcd

# Описание правил игры
brain_games.scripts.module.describe_rules('Find the greatest '
                                          'common divisor of given numbers.')


# Счетчик
def counts():
    i = 1

    while i <= 3:
        RANDOM_NUMBER_FIRST = randint(1, 100)
        RANDOM_NUMBER_SECOND = randint(1, 100)

        QUESTION = str(RANDOM_NUMBER_FIRST) + ' ' + str(RANDOM_NUMBER_SECOND)

        # Задаем переменную correct_answer
        brain_games.scripts.module.correct_answer = str(gcd(RANDOM_NUMBER_FIRST,
                                                        RANDOM_NUMBER_SECOND))

        # Вопрос игроку
        brain_games.scripts.module.ask_question(QUESTION)

        # Поле для ввода ответа
        user_answer = input("Your answer: ")

        # Проверка правильности ответа
        brain_games.scripts.module.checked_user_answer(user_answer)

        i += 1

    brain_games.scripts.module.congratulate(brain_games.scripts.module.name)


def main():
    counts()


if __name__ == '__main__':
    main()
