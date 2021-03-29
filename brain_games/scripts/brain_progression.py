#!/usr/bin/env python
import brain_games.engine
from brain_games.games.brain_progression import MISSED_NUMBER
from brain_games.games.brain_progression import generate_progression
import random


# Описание правил игры
brain_games.engine.describe_game('What number is missing in the progression?')


# Счетчик
def counts():
    ROUNDS_COUNT = 3
    i = 1

    while i <= ROUNDS_COUNT:

        # Вопрос игроку
        brain_games.engine.number = generate_progression(random.randint(1, 10), random.randint(1, 6), random.randint(6, 10))

        # Задаем значение переменной correct_answer
        brain_games.engine.correct_answer = ANSWER

        brain_games.engine.count()

        i += 1


    print('Congratulations, {}!'.format(brain_games.engine.name))


def main():
    counts()


if __name__ == '__main__':
    main()
