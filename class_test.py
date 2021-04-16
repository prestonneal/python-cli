# broken: python example.py add 10 20
# fix it: python example.py add 10 20 --offset=0

import fire

class BrokenCalculator(object):

  def __init__(self, offset=1):
      self._offset = offset

  def add(self, x, y):
    return x + y

  def multiply(self, x, y):
    return x * y

if __name__ == '__main__':
  fire.Fire(BrokenCalculator)
