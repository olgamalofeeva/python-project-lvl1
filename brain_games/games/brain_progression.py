import random
MISSED_NUMBER = random.randint(1, 5)

def generate_progression(start, step, limit):
  RANGE_NUMBERS = [i for i in range(start, start + step * limit, step)]
  RANGE_NUMBERS[MISSED_NUMBER] = '..'

  return ' '.join(map(str, RANGE_NUMBERS))

ANSWER = str(RANGE_NUMBERS[MISSED_NUMBER - 1] + step)



