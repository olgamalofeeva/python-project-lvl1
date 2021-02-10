#!/usr/bin/env python
import prompt
from random import randint

def greet():
    print('Welcome to the Brain Games!')


greet()

name = prompt.string('May I have your name? ')


def welcome_user():
    print('Hello, ' + name + '!')

welcome_user()

print('Answer "yes" if the number is even, otherwise answer "no".')

def game_description():
  i = 1

  while i <= 3:
    random_number = randint(1, 100)
    print('Question: ' + str(random_number))
    user_answer = input("Your answer: ")

    if random_number % 2 == 0 and user_answer == 'yes' or random_number % 2 != 0 and user_answer == 'no':
        print('Correct!') 
    
    else:
        print("'{}' is wrong answer. Correct answer was '{}'.\nLet's try again, {}!".format(user_answer, 00, name))
        exit()
    i += 1
  
  print('Congratulations,{}!'.format(name))

def main():
    game_description()


if __name__ == '__main__':
    main()