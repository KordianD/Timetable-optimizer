import numpy as np
import pandas as pd

class Student:
    def __init__(self, id, first_name='Jan', last_name='Kowalski'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Subject:
    def __init__(self, name, num_of_terms=4):
        self.name = name
        self.num_of_terms = num_of_terms

NUM_OF_STUDENTS = 50
NAMES_OF_SUBJECTS = ['Sieci komputerowe', 'Systemy pomiarowe', 'Teoria sterowania', 'Badania operacyjne',
                     'Technika mikroprocesorowa', 'Podstawy robotyki', 'Teoria optymalizacji']

students = [Student(id) for id in range(0, NUM_OF_STUDENTS)]
subjects = [Subject(nameOfSubject) for nameOfSubject in NAMES_OF_SUBJECTS]