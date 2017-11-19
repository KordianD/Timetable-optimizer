import numpy as np
import pandas as pd
from Student import Student
from Subject import Subject


NUM_OF_STUDENTS = 50
MAX_NUMBER_ENCODED = 44
NAMES_OF_SUBJECTS = ['Sieci komputerowe', 'Systemy pomiarowe', 'Teoria sterowania', 'Badania operacyjne',
                     'Technika mikroprocesorowa', 'Podstawy robotyki', 'Teoria optymalizacji']

class Bee():
    def __init__(self, num_of_students, names_of_subjects):
        self.students = [Student(id) for id in range(num_of_students)]
        self.subjects = [Subject(name_of_subject) for name_of_subject in names_of_subjects]

    def generate_solution(self):
        for student in self.students:
            student.timetable = generate_random_timetable(self.subjects)


def generate_random_timetable(subjects):
    random_timetable = []
    for _ in range(len(subjects)):
        random_timetable.append(np.random.random_integers(0, MAX_NUMBER_ENCODED))

    return random_timetable