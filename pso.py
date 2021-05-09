import random
import copy

from particle import Particle
from population import Population

class Pso:
    def __init__(self, population, iterations):
      self.population = population
      self.iterations = iterations
      
      self.const = 2.05 # sugerido por Eberhart e Kennedy (ver no readme)
      self.w = 0.5 # sugerido por Eberhart e Kennedy (ver no readme)

    def check_speed(self, speed):
      if (speed >= -77) and (speed <= 77):
        right_speed = speed
      elif (speed <= -77):
        right_speed = -77
      else:
        right_speed = 77
      
      return right_speed

    def check_position(self, position, speed):
      if (position >= -512) and (position <= 512):
        right_position = position
      elif (position <= -512):
        right_position = -512
        speed = 0
      elif (position >= 512):
        right_position = 512
        speed = 0
      
      return right_position, speed
    
    def execute(self):
      best = []

      population_list = Population(self.population).start_population()

      for i in range(self.iterations):

        for particle in population_list:
          fitness = particle.run_fitness()
          
          if (fitness < particle.get_fitness()):
            particle.set_fitness(fitness)
            particle.set_better(particle.x, particle.y)

        sorted_population = list(population_list)
        sorted_population = sorted(sorted_population , key=Particle.get_fitness)
        
        g_best = sorted_population[0]

        best.append(copy.copy(g_best))
        
        for particle in population_list:
          x_speed = self.w * particle.x_speed + self.const * random.uniform(0,1) * (particle.x_best - particle.x) + \
                    self.const * random.uniform(0,1) * (g_best.x_best - particle.x_best)

          speed = self.check_speed(x_speed)
          particle.set_x_speed(speed)

          new_x_position = particle.x + x_speed

          position, speed = self.check_position(new_x_position, x_speed)
          particle.set_x_speed(speed)
          particle.x = position

          y_speed = self.w * particle.y_speed + self.const * random.uniform(0,1) * (particle.y_best - particle.y) + \
                    self.const * random.uniform(0,1) * (g_best.y_best - particle.y_best)

          speed = self.check_speed(y_speed)
          particle.set_y_speed(speed)

          new_y_position = particle.y + y_speed

          position, speed = self.check_position(new_y_position, y_speed)
          particle.set_y_speed(speed)
          particle.y = position
              
      return best
