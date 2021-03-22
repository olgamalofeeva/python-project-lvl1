#!/usr/bin/env python
import brain_games.scripts.module
import random

# Описание правил игры
brain_games.scripts.module.describe_rules('What number '
                                          'is missing in the progression?')


# Счетчик
def counts():
    i = 1

    while i <= 3:
        START = random.randint(1, 10)
        STEP = random.randint(1, 6)
        LIMIT = random.randint(6, 10)
        MISSED_NUMBER = random.randint(1, 5)

        RANGE_NUMBERS = [i for i in range(START, START + STEP * LIMIT, STEP)]
        RANGE_NUMBERS[MISSED_NUMBER] = '..'

        PROGRESSION = ' '.join(map(str, RANGE_NUMBERS))

        # Задаем значение переменной correct_answer
        brain_games.scripts.module.correct_answer = str(RANGE_NUMBERS
                                                        [MISSED_NUMBER - 1] +
                                                        + STEP)

        # Вопрос игроку
        brain_games.scripts.module.ask_question(PROGRESSION)

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
