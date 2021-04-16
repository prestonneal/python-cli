# python multiple_test.py add 10 10
# python multiple_test.py multiply 10 20

import fire

def add(x, y):
  return x + y

def multiply(x, y):
  return x * y

if __name__ == '__main__':
  fire.Fire()
