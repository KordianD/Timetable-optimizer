import numpy as np

class Student:
    def __init__(self, id, first_name='Jan', last_name='Kowalski'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.timetable = {}

    def generate_random_timetable(self, subjects):
        for subject in subjects:
            self.timetable[subject.name] = subject.terms[np.random.random_integers(0, len(subject.terms) - 1)]
		