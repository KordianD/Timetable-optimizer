from src.Student import Student
from src.Subject import Subject


class Bee:
    def __init__(self, num_of_students, names_of_subjects):
        self.students = [Student(id) for id in range(num_of_students)]
        self.subjects = [Subject(name_of_subject) for name_of_subject in names_of_subjects]
        self.fitness = 0

    def generate_random_solution(self):
        for subject in self.subjects:
            subject.generate_random_terms()
        
        for student in self.students:
            student.generate_random_timetable(self.subjects)

    def calculate_bee_fitness(self):
        for student in self.students:
            self.fitness += student.calculate_student_fitness()
