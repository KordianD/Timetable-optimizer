import numpy as np
from Classwork import Classwork
from configuration import *


class Subject:
    def __init__(self, name, num_of_terms=4):
        self.name = name
        self.num_of_terms = num_of_terms
        self.terms = []

    def generate_random_terms(self, search_space):
        for _ in range(self.num_of_terms):
            random_date = (np.random.random_integers(min(DAYS_SPACE), max(DAYS_SPACE),
                               np.random.random_integers(min(HOURS_SPACE)), max(HOURS_SPACE)))

            self.terms.append(Classwork(self.name, random_date))
