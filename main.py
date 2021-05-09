
import test2csv

from pso import Pso

def main():
  executions = 10
  iterations = [20, 50, 100]
  populations = [50, 100]

  for iteration in iterations:
    for population in populations:
      
      file_name = "{}it-{}pop-{}".format(iteration, population, executions)
      result_list = []

      for execution in range(executions):
  
        result = Pso(iteration, population).execute()
        result_list.append(result)

      test2csv.save('results/' + file_name, result_list)

if __name__ == "__main__":
  main()