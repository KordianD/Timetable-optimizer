from src.Student import Student
from src.Subject import Subject
import random


class Bee:
    def __init__(self, num_of_students, names_of_subjects):
        self.students = [Student(id) for id in range(num_of_students)]
        self.subjects = [Subject(name_of_subject, index) for index, name_of_subject in enumerate(names_of_subjects)]
        self.fitness = 0

        for subject in self.subjects:
            subject.generate_random_terms()

        for student in self.students:
            student.generate_random_timetable(self.subjects)

    def calculate_bee_fitness(self):
        fitness = 0
        for student in self.students:
            fitness += student.calculate_student_fitness()
        self.fitness = fitness

    def get_random_student(self):
        return random.choice(self.students)
