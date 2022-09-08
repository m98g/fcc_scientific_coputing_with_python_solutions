class Hat:

  def __init__(self, **kwargs):
    list_ = list()

    for x, y in kwargs.items():
      for i in range(y):
        list_.append(x)
    
    self.contents = list_

  def draw(self, to_draw):
    if to_draw > len(self.contents):
      return(self.contents)
    else:
      balls = list()
      # somethig here is wrong
      # with the copy method we have the problem that the contents is not reduced but 
      # now we have the problem that there should be not a 
      for i in range(to_draw):
        ran = random.randint(0, len(self.contents) - 1)
        balls.append(self.contents.pop(ran))
      return(balls)

  def to_draw_copy(self, to_draw):
    if to_draw > len(self.contents):
      return(self.contents)
    else:
      balls = list()
      list__ = self.contents.copy()
      for i in range(to_draw):
        ran = random.randint(0, len(list__) - 1)
        balls.append(list__.pop(ran))
      return(balls)

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    got_this = hat.to_draw_copy(num_balls_drawn)
    flag = False
    for x, y in expected_balls.items():
      if got_this.count(x) >= y:
        flag = True
      else:
        flag = False
        break

    if flag == True:
      count += 1
        
  return(count / num_experiments)
