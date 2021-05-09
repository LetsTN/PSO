import math

class Particle:
  def __init__(self, x, y, x_speed, y_speed):
    self.x = x
    self.y = y
    
    self.x_speed = x_speed
    self.y_speed = y_speed

    self.fitness = None

    self.x_best = x
    self.y_best = y
  
  
  def run_fitness(self):
    return - (self.y + 47) * math.sin(abs(((self.x/2) + (self.y + 47))) ** (1/2)) - self.x * math.sin((abs(self.x - (self.y + 47)) ** (1/2)))

  def set_better(self, x, y):
    self.x_best = x
    self.y_best = y
  
  def set_fitness(self, fitness):
    self.fitness = fitness
  
  def get_fitness(self):
    return self.fitness

  def set_x_speed(self, x_speed):
    self.x_speed = x_speed
  
  def set_y_speed(self, y_speed):
    self.y_speed = y_speed
