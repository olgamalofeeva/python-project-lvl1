#!/usr/bin/env python
import prompt
import random

def greet():
    print('Welcome to the Brain Games!')


greet()

name = prompt.string('May I have your name? ')


def welcome_user():
    print('Hello, ' + name + '!')

welcome_user()

print('What number is missing in the progression?')

def game_description():
  i = 1

  while i <= 3:
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    limit = 10
    missed_number = random.randint(1, 9)

    range_numbers = [i for i in range(start, start + step * limit, step)]
    range_numbers[missed_number] = '...'


    print('Question: ' + ' '.join(map(str, range_numbers)))
    user_answer = input("Your answer: ")
    
    correct_answer = range_numbers[missed_number - 1] + step

    if int(user_answer) == correct_answer:
        print('Correct!') 
    
    else:
        print("'{}' is wrong answer. Correct answer was '{}'.\nLet's try again, {}!".format(user_answer, correct_answer, name))
        quit()
    i += 1
  
  print('Congratulations,{}!'.format(name))

def main():
    game_description()


if __name__ == '__main__':
    main()