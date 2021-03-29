#!/usr/bin/env python
import brain_games.engine
from random import randint
from brain_games.games.brain_prime import is_Prime

# Описание правил игры
brain_games.engine.describe_game('Answer "yes" if given number is prime. Otherwise answer "no".')


# Счетчик
def counts():
    ROUNDS_COUNT = 3
    i = 1

    while i <= ROUNDS_COUNT:

        brain_games.engine.number = randint(1, 100)

        # Задаем значение переменной correct_answer
        brain_games.engine.correct_answer = 'yes' if is_Prime(brain_games.engine.number) else 'no'

        brain_games.engine.count()

        i += 1


    print('Congratulations, {}!'.format(brain_games.engine.name))

def main():
    counts()


if __name__ == '__main__':
    main()
