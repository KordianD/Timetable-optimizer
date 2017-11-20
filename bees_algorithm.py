from Student import Student
from Subject import Subject
from configuration import *


class Population:
    def __init__(self, num_of_bees, num_of_students, names_of_subjects):
        self.num_of_bees = num_of_bees
        self.bees = [Bee(num_of_students, names_of_subjects) for _ in range(num_of_bees)]
        
    def generate_random_population(self, search_space):
        for bee in self.bees:
            bee.generate_random_solution(search_space)

    def calculate_fitness(self):
        pass
