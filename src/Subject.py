import numpy as np
from src.Classwork import Classwork
from src.configuration import *


class Subject:
    def __init__(self, name, num_of_terms=4):
        self.name = name
        self.num_of_terms = num_of_terms
        self.terms = []

    def generate_random_terms(self):
        for _ in range(self.num_of_terms):

            random_day = np.random.random_integers(min(DAYS_SPACE), max(DAYS_SPACE))
            random_hour = np.random.random_integers(min(HOURS_SPACE), max(HOURS_SPACE))

            self.terms.append(Classwork(self.name, random_day, random_hour))
