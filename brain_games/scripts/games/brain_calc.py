#!/usr/bin/env python
import brain_games.scripts.module
import random
import operator


# Описание правил игры
brain_games.scripts.module.describe_rules('What is the result of the '
                                          'expression?')


# Счетчик
def counts():
    i = 1

    while i <= 3:
        RANDOM_NUMBER_FIRST = random.randint(50, 100)
        RANDOM_NUMBER_SECOND = random.randint(1, 50)

        OPERATORS = [('+', operator.add), ('-', operator.sub),
                     ('*', operator.mul)]
        picked_operator, fn = random.choice(OPERATORS)

        QUESTION = '{} {} {}'.format(RANDOM_NUMBER_FIRST, picked_operator,
                                     RANDOM_NUMBER_SECOND)

        # Задаем значение переменной correct_answer
        brain_games.scripts.module.correct_answer = str(fn(RANDOM_NUMBER_FIRST,
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
