import numpy as np


class Subject:
    def __init__(self, name, num_of_terms=4):
        self.name = name
        self.num_of_terms = num_of_terms
        self.terms = []

    def generate_random_terms(self, search_space):
        for _ in range(self.num_of_terms):
            self.terms.append((np.random.random_integers(search_space[0][0], search_space[0][1]),
                               np.random.random_integers(search_space[1][0], search_space[1][1])))
