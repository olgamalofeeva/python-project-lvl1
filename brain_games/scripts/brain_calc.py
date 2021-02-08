#!/usr/bin/env python
import prompt
import random
import operator

def greet():
    print('Welcome to the Brain Games!')


greet()

name = prompt.string('May I have your name? ')


def welcome_user():
    print('Hello, ' + name + '!')

welcome_user()

print('What is the result of the expression?')

def game_description():
  i = 1

  while i <= 3:
    random_number_first = random.randint(50, 100)
    random_number_second = random.randint(1, 50)
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    picked_operator, fn = random.choice(operators)
    print('Question: {} {} {}'.format(random_number_first, picked_operator, random_number_second))
    user_answer = input("Your answer: ")
    
    if int(user_answer) == fn(random_number_first, random_number_second):
        print('Correct!') 

    else:
        print("'{}' is wrong answer. Correct answer was '{}'.\nLet's try again, {}!".format(user_answer, fn(random_number_first, random_number_second), name))
        exit()
    i += 1
  print('Congratulations,{}!'.format(name))

def main():
    game_description()


if __name__ == '__main__':
    main()