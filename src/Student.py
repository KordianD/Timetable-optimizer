import random
import src.configuration as conf


class Student:
    def __init__(self, id, first_name='Jan', last_name='Kowalski'):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.timetable = []
        self.fitness = 0

    def generate_random_timetable(self, subjects):
        for subject in subjects:
            self.timetable.append(random.choice(subject.terms))

    def calculate_student_fitness(self):
        fitness = 0
        for day in conf.DAYS_SPACE:
            day_classwork = self.get_classwork_from_one_day(day)
            fitness += self.calculate_day_overlapping(day_classwork)

        return fitness

    def get_classwork_from_one_day(self, day):
        classwork_day = [classwork for classwork in self.timetable if classwork.day == day]
        return sorted(classwork_day, key=lambda x: x.hour)

    def calculate_day_overlapping(self, day_classwork):
        overlapped_in_minutes = []
        for index in range(len(day_classwork)):
            self.calculate_difference_for_one_classwork(day_classwork, overlapped_in_minutes, index)

        return sum(overlapped_in_minutes)

    def calculate_difference_for_one_classwork(self, day_classwork, overlapped_in_minutes, classwork_index):
        for index in range(classwork_index, len(day_classwork)):
            if index != classwork_index:
                slot_difference = abs(day_classwork[index].hour - day_classwork[classwork_index].hour)
                if slot_difference < conf.TIME_SLOTS:
                    overlapped_in_minutes.append((conf.SLOTS_DURING_ONE_CLASSWORK - slot_difference) *
                                                 conf.DIFFERENCE_BETWEEN_STARTING_CLASSES)
