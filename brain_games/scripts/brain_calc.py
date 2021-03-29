#!/usr/bin/env python
import brain_games.engine
import random
import operator


# Описание правил игры
brain_games.engine.describe_game('What is the result of the expression?')


# Счетчик
def counts():
    ROUNDS_COUNT = 3
    i = 1

    while i <= ROUNDS_COUNT:
        RANDOM_NUMBER_FIRST = random.randint(50, 100)
        RANDOM_NUMBER_SECOND = random.randint(1, 50)

        OPERATORS = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
        picked_operator, fn = random.choice(OPERATORS)
        
        brain_games.engine.number = '{} {} {}'.format(RANDOM_NUMBER_FIRST, picked_operator, RANDOM_NUMBER_SECOND)

        # Задаем значение переменной correct_answer
        brain_games.engine.correct_answer = str(fn(RANDOM_NUMBER_FIRST, RANDOM_NUMBER_SECOND))

        brain_games.engine.count()

        i += 1


    print('Congratulations, {}!'.format(brain_games.engine.name))


def main():
    counts()


if __name__ == '__main__':
    main()
