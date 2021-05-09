import statistics

from particle import Particle

def save(file_name, results):  
  with open(file_name + '.csv', 'w+') as txt_file:
    txt_file.write(',')    

    for i in range(len(results)):
      txt_file.write('Teste ' + num2str(i+1) + ', ')    

    txt_file.write('Média, ')
    txt_file.write('Melhor, ')
    txt_file.write('x_best, ')
    txt_file.write('y_best')

    txt_file.write('\n')

    for i in range(len(results)):
      data = []
      data_particle = []

      txt_file.write('gBest' + num2str(i+1) + ', ')

      for result in results:
        cell = round(result[i].fitness, 4)
        data.append(cell)
        data_particle.append(result[i])
        txt_file.write(str(cell) + ', ')

      data_list = sorted(data_particle , key=Particle.get_fitness)

      media = statistics.mean(data)
      txt_file.write(str(round(media, 4)) + ', ')

      best = data_list[0].get_fitness()
      txt_file.write(str(round(best, 4)) + ', ')

      x_best = data_list[0].x_best
      txt_file.write(str(round(x_best, 4)) + ', ')

      y_best = data_list[0].y_best
      txt_file.write(str(round(y_best, 4)))

      txt_file.write('\n')

def num2str(num):
  if num<10:
    return '0'+str(num)
  return str(num)