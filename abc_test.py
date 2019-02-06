import os
import numpy as np
from bee_colony import utilities
from bee_colony.abc import BeeColony
RANGE = 5
BEE_FACTOR = 20




# func_list = ["rosenbrock"]

func_list = ["alpine", "rosenbrock", "rastrigin",  "sphere"]
class TestFunctions:
    def alpine(self, vector):
        vector = self.convert_vector(vector)
        return np.sum(np.abs(vector * np.sin(vector) + 0.1 * vector))


    def two_n_minima(self,vector):
        vector = self.convert_vector(vector)
        return np.sum(np.square(np.square(vector)) - 16 * np.square(vector) + 5 * vector)


    def rosenbrock(self,vector, a=1, b=100):
        vector = self.convert_vector(vector)
        return (a - vector[0]) ** 2 + b * (vector[1] - vector[0] ** 2) ** 2


    def rastrigin(self,vector):
        vector = self.convert_vector(vector)
        return 10 * vector.size + sum(vector * vector - 10 * np.cos(2 * np.pi * vector))


    def styblinski_tang(self,vector):
        vector = self.convert_vector(vector)
        return sum(vector ^ 4 - 16 * vector ^ 2 + 5 * vector) / 2


    def sphere(self,vector):
        vector = self.convert_vector(vector)
        return sum(vector * vector)


    def convert_vector(self,vector):
        return np.array(vector)


def run():
    lower_limit = [0, 2]
    up_limit = [10, 12]
    bees = [10,50,100]
    for func in func_list:

        for i in range(len(lower_limit)):
            for bee in bees:
                model = BeeColony(
                                    lower=[lower_limit[i]] * 2,
                                      upper=[up_limit[i]]*2,
                                      fun=getattr(TestFunctions(), func),
                                      numb_bees=bee,
                                      max_itrs=100,
                                      verbose=False)

                results = model.run()
                if not os.path.exists('results'):
                    os.makedirs('results')

                if not os.path.exists(os.path.join('results', func)):
                    os.makedirs(os.path.join('results', func))

                res_name = func+"_bee_"+str(bee)+"_low_limit_"+str(lower_limit[i])+"_up_limit_"+str(lower_limit[i])
                print("Fitness for {3}  ABC: {0} in x,y ({1},{2}) ".format(model.best, model.solution[0], model.solution[1], res_name ) )
                res_name = os.path.join('results', func, res_name)
                utilities.plot(results, res_name)



if __name__ == "__main__":
    run()
