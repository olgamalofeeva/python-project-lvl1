#!/usr/bin/env python
import prompt
from random import randint
from math import gcd 

def greet():
    print('Welcome to the Brain Games!')


greet()

name = prompt.string('May I have your name? ')


def welcome_user():
    print('Hello, ' + name + '!')

welcome_user()

print('Find the greatest common divisor of given numbers.')

def game_description():
  i = 1

  while i <= 3:
    random_number_first = randint(1, 100)
    random_number_second = randint(1, 100)
    print('Question: ' + str(random_number_first) + ' ' + str(random_number_second))
    user_answer = input("Your answer: ")

    if int(user_answer) == gcd(random_number_first, random_number_second):
        print('Correct!') 
    
    else:
        print("'{}' is wrong answer. Correct answer was '{}'.\nLet's try again, {}!".format(user_answer, gcd(random_number_first, random_number_second), name))
        exit()
    i += 1
  
  print('Congratulations,{}!'.format(name))

def main():
    game_description()


if __name__ == '__main__':
    main()