#!/usr/bin/env python
import prompt

#Приветствие
def greet(greeting):
    print(greeting)


greet('Welcome to the Brain Games!')

name = prompt.string('May I have your name? ')


def welcome_user(who):
    print('Hello, {}!'.format(who))


welcome_user(name)

#Описание правил игры
def describe_rules(rules):
    print(rules)

#Вопрос игроку
def ask_question(question):
        print('Question: {}'.format(question))
        

def checked_user_answer(user_answer):
    if user_answer == correct_answer:
        print('Correct!') 
    
    else:
        print("'{}' is wrong answer. Correct answer was '{}'.\nLet's try again, {}!".format(user_answer, correct_answer, name))
        quit()

def congratulate(name):
    print('Congratulations,{}!'.format(name))

