import random
from Classwork import Classwork


class Student:
    def __init__(self, id, first_name='Jan', last_name='Kowalski'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.timetable = []

    def generate_random_timetable(self, subjects):
        for subject in subjects:
            self.timetable.append(Classwork(subject.name, random.choice(subject.terms)))

    def calculate_student_fitness(self):
        list_of_days = self.get_days_from_timetable()
        fitness = 0

        for day in list_of_days:
            class_hours = [hour for hour in list_of_days]
