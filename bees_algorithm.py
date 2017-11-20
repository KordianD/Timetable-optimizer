import numpy as np
import pandas as pd
from Student import Student
from Subject import Subject

# Configuration
NUM_OF_STUDENTS = 50
MAX_NUMBER_ENCODED = 44
NUM_OF_BEES = 45
NUM_OF_SITES = 3
MAX_GENS = 500
NAMES_OF_SUBJECTS = ['Sieci komputerowe', 'Systemy pomiarowe', 'Teoria sterowania', 'Badania operacyjne',
                     'Technika mikroprocesorowa', 'Podstawy robotyki', 'Teoria optymalizacji']
SEARCH_SPACE = [[0, 4], [0, 39]]

class Bee():
    def __init__(self, num_of_students, names_of_subjects):
        self.students = [Student(id) for id in range(num_of_students)]
        self.subjects = [Subject(name_of_subject) for name_of_subject in names_of_subjects]

    def generate_random_solution(self, search_space):
        for subject in self.subjects:
            subject.generate_random_terms(search_space)
        
        for student in self.students:
            student.generate_random_timetable(self.subjects)

class Population:
    def __init__(self, num_of_bees, num_of_students, names_of_subjects):
        self.num_of_bees = num_of_bees
        self.bees = [Bee(num_of_students, names_of_subjects) for _ in range(num_of_bees)]
        
    def generate_random_population(self, search_space):
        for bee in self.bees:
            bee.generate_random_solution(search_space)

#def generate_random_timetable(subjects):
#    random_timetable = []
#    for _ in range(len(subjects)):
#        random_timetable.append(np.random.random_integers(0, MAX_NUMBER_ENCODED))
#
#    return random_timetable
