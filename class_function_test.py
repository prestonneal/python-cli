# python example.py --name="Sherrerd Hall" --stories=3 climb_stairs 10
# python example.py --name="Sherrerd Hall" climb_stairs --stairs_per_story=10
# python example.py --name="Sherrerd Hall" climb_stairs --stairs-per-story 10
# python example.py climb-stairs --stairs-per-story 10 --name="Sherrerd Hall"

import fire

class Building(object):

  def __init__(self, name, stories=1):
    self.name = name
    self.stories = stories

  def climb_stairs(self, stairs_per_story=10):
    for story in range(self.stories):
      for stair in range(1, stairs_per_story):
        yield stair
      yield 'Phew!'
    yield 'Done!'

if __name__ == '__main__':
  fire.Fire(Building)
