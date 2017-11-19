import numpy as np
import pandas as pd
from Student import Student
from Subject import Subject

NUM_OF_STUDENTS = 50
NAMES_OF_SUBJECTS = ['Sieci komputerowe', 'Systemy pomiarowe', 'Teoria sterowania', 'Badania operacyjne',
                     'Technika mikroprocesorowa', 'Podstawy robotyki', 'Teoria optymalizacji']

students = [Student(id) for id in range(NUM_OF_STUDENTS)]
subjects = [Subject(nameOfSubject) for nameOfSubject in NAMES_OF_SUBJECTS]
