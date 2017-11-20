import numpy as np
import random

class Student:
    def __init__(self, id, first_name='Jan', last_name='Kowalski'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.timetable = {}

    def generate_random_timetable(self, subjects):
        for subject in subjects:
            self.timetable[subject.name] = random.choice(subject.terms)

    def calculate_student_fitness(self):
        pass