import copy
from collections import Counter
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = self.create_list(locals()['kwargs'])

  def create_list(self, arguments):
    contents = []
    for key in arguments:
      for i in range(arguments[key]):
        contents.append(key)
    return contents

  def draw(self, number_of_balls):
    if number_of_balls >= len(self.contents):
      return self.contents
    choices = []
    for i in range(number_of_balls):
      choices.append(self.contents.pop(self.contents.index(random.choice(self.contents))))
    return choices
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  times_correct = 0
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_list = hat_copy.draw(num_balls_drawn)
    drawn = Counter(drawn_list)
    is_correct = True
    for key, val in expected_balls.items():
      if key not in drawn.keys():
        is_correct = False
        break
      try:
        if drawn[key] < val:
          is_correct = False
      except KeyError:
        continue
    if is_correct:
      times_correct += 1
  return times_correct/num_experiments