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

print('Answer "yes" if given number is prime. Otherwise answer "no".')

def game_description():
  d = 1

  while d <= 3:
    random_number = randint(1, 100)
    print('Question: ' + str(random_number))
    user_answer = input("Your answer: ")

    def isPrime(n):
        i = 2
        while n % i != 0:          
          i += 1
        return i == n
    isPrime(random_number)

    if isPrime(random_number) is True and user_answer == 'yes' or isPrime(random_number) is not True and user_answer == 'no':
        print('Correct!')

    else:
        print("'{}' is wrong answer. Correct answer was '{}'.\nLet's try again, {}!".format(user_answer, 00, name))
        quit()

      
    d += 1
  
  print('Congratulations,{}!'.format(name))

def main():
    game_description()


if __name__ == '__main__':
    main()