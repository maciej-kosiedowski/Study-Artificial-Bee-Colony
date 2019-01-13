import numpy as np

RANGE = 5
BEE_FACTOR = 20

bees_population = [x * BEE_FACTOR for x in range(0, RANGE)]
lower_limit = np.random(RANGE)

func_list = ["alpine", "two_n_minima", "rosenbrock", "rastrigin", "styblinski_tang", "sphere"]


def alpine(vector):
    return np.sum(np.abs(vector * np.sin(vector) + 0.1 * vector))


def two_n_minima(vector):
    return np.sum(np.square(np.square(vector)) - 16 * np.square(vector) + 5 * vector)


def rosenbrock(vector, a=1, b=100):
    return (a - vector[0]) ** 2 + b * (vector[1] - vector[0] ** 2) ** 2


def rastrigin(vector):
    return 10 * vector.size + sum(vector * vector - 10 * np.cos(2 * np.pi * vector))


def styblinski_tang(vector):
    return sum(vector ^ 4 - 16 * vector ^ 2 + 5 * vector) / 2


def sphere(vector):
    return sum(vector * vector)


def convert_vector_to_np(vector):
    return np.array(vector)
