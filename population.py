import random

from particle import Particle

class Population:
  def __init__(self, population):
    self.population = population

    self.x_speed = random.uniform(-77, 77)
    self.y_speed = random.uniform(-77, 77)

  def start_population(self):
    population_list = []

    for i in range(self.population):
      x = random.uniform(-512, 512)
      y = random.uniform(-512, 512)

      particle = Particle(x, y, self.x_speed, self.y_speed)
      fitness = particle.run_fitness()
      particle.set_fitness(fitness)

      population_list.append(particle)

    return population_list
