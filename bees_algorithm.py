import numpy as np
import pandas as pd

class Student:
	def __init__(self, id, firstName='Jan', lastName='Kowalski'):
		self.id = id
		self.firstName = firstName
		self.lastName = lastName
		
class Subject:
	def __init__(self, name, numOfTerms=4):
		self.name = name
		self.numOfTerms = numOfTerms
		
numOfStudents = 50
namesOfSubjects = ['Sieci komputerowe', 'Systemy pomiarowe', 'Teoria sterowania', 'Badania operacyjne',
    				    'Technika mikroprocesorowa', 'Podstawy robotyki', 'Teoria optymalizacji']
				   
students = [Student(id) for id in range(0, numOfStudents)]
subjects = [Subject(nameOfSubject) for nameOfSubject in namesOfSubjects]