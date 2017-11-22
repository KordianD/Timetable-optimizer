import random
from src.configuration import *


class Student:
    def __init__(self, id, first_name='Jan', last_name='Kowalski'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.timetable = []

    def generate_random_timetable(self, subjects):
        for subject in subjects:
            self.timetable.append(random.choice(subject.terms))

    def calculate_student_fitness(self):
        fitness = 0
        for day in DAYS_SPACE:
            day_classwork = self.get_classwork_from_one_day(day)

    def get_classwork_from_one_day(self, day):
        classwork_day = [classwork for classwork in self.timetable if classwork.day == day]
        return sorted(classwork_day, key=lambda x: x.day)

    def calculate_day_overlapping(self, day_classwork):
        overlapped_in_minutes = 0
        for index, starting_hour in enumerate(day_classwork[:-1]):
            for elem in day_classwork[:-1]:
                slot_difference = day_classwork[index+1].day - day_classwork[index].day
                if slot_difference < TIME_SLOTS:
                    overlapped_in_minutes += slot_difference * DIFFERENCE_BETWEEN_STARTING_CLASSES

        return overlapped_in_minutes
