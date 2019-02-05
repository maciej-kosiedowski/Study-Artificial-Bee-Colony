#!/usr/bin/env python


import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def plot(data, func_name):
    font = FontProperties()
    font.set_size('larger')
    plt.figure(1, figsize=(21,14))

    plt.subplot(221)
    plt.plot(data["all_population_func_x"], data["all_population_func_y"], 'ro', markersize=1)
    plt.yscale('linear')
    plt.title('Positions of all bees')
    plt.grid(True)

    plt.subplot(222)
    plt.scatter(data["all_population_func_x"], data["all_population_func_y"], data["all_population_func_value"])
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title('Bee positions along with the value of the objective function. If it`s bigger, better minimum')
    plt.grid()

    plt.subplot(223)
    plt.plot(range(len(data["best"])), data["best"])
    plt.xlabel("Iteration #")
    plt.ylabel("Value [-]")
    plt.title('Value of the objective function')
    plt.grid()

    plt.subplot(224)
    plt.plot(range(len(data["mean"])), data["mean"])
    plt.xlabel("Iteration #")
    plt.ylabel("Mean value of bees for objective function ")
    plt.title('Mean values of bees for objective function')
    plt.grid()




    plt.savefig(func_name + '.png')
    plt.clf()

