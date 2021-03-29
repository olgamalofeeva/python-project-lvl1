#!/usr/bin/env python
import brain_games.engine
from random import randint
from math import gcd

# Описание правил игры
brain_games.engine.describe_game('Find the greatest common divisor of given numbers.')


# Счетчик
def counts():
    ROUNDS_COUNT = 3
    i = 1

    while i <= ROUNDS_COUNT:
        RANDOM_NUMBER_FIRST = randint(1, 100)
        RANDOM_NUMBER_SECOND = randint(1, 100)

        brain_games.engine.number = str(RANDOM_NUMBER_FIRST) + ' ' + str(RANDOM_NUMBER_SECOND)

        # Задаем переменную correct_answer
        brain_games.engine.correct_answer = str(gcd(RANDOM_NUMBER_FIRST, RANDOM_NUMBER_SECOND))

        brain_games.engine.count()

        i += 1

    print('Congratulations, {}!'.format(brain_games.engine.name))

def main():
    counts()


if __name__ == '__main__':
    main()
