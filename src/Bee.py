from src.Student import Student
from src.Subject import Subject


class Bee:
    def __init__(self, num_of_students, names_of_subjects):
        self.students = [Student(id) for id in range(num_of_students)]
        self.subjects = [Subject(name_of_subject) for name_of_subject in names_of_subjects]
        self.fitness = 0

        for subject in self.subjects:
            subject.generate_random_terms()

        for student in self.students:
            student.generate_random_timetable()

    def calculate_bee_fitness(self):
        fitness = 0
        for student in self.students:
            fitness += student.calculate_student_fitness()
        return fitness