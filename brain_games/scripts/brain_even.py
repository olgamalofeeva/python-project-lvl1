#!/usr/bin/env python
import brain_games.engine
from brain_games.games.brain_even import is_even 
from random import randint

brain_games.engine.describe_game('Answer "yes" if the number is even, otherwise answer "no".')

def counts():
    ROUNDS_COUNT = 3
    i = 1

    while i <= ROUNDS_COUNT:
        brain_games.engine.number = randint(1, 100)

        # Задаем значение переменной correct_answer
        brain_games.engine.correct_answer = 'yes' if is_even(brain_games.engine.number) else 'no'

        brain_games.engine.count()
        
        i += 1


    print('Congratulations, {}!'.format(brain_games.engine.name))


def main():
    counts()


if __name__ == '__main__':
    main()