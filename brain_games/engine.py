import prompt


# Приветствие
def greet(greeting):
    print(greeting)


greet('Welcome to the Brain Games!')

name = prompt.string('May I have your name? ')


def welcome_user(who):
    print('Hello, {}!'.format(who))


welcome_user(name)


# Описание правил игры
def describe_game(description):
    print(description)


def count():
# Вопрос игроку
  print('Question: {}'.format(number))  

# Поле для ввода ответа
  user_answer = input("Your answer: ")

  if user_answer == correct_answer:
      print('Correct!')

  else:
    print("'{}' is wrong answer. Correct answer was '{}'.\nLet's try again, {}!".format(user_answer, correct_answer, name))
    quit()


  
