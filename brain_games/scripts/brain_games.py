#!/usr/bin/env python
import prompt


def greet():
    print('Welcome to the Brain Games!')


greet()

name = prompt.string('May I have your name? ')


def welcome_user():
    print('Hello, ' + name + '!')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
