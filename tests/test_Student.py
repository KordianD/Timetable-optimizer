import pytest
from src.Student import Student
from src.Subject import Subject
from src.Classwork import Classwork

sub = Subject('First')


def test_calculate_day_overlapping_with_no_overlapping():
    classwork1 = Classwork('First_classwork', random_day=0, random_hour=5)
    classwork2 = Classwork('Second_classwork', random_day=0, random_hour=15)
    classwork3 = Classwork('Third_classwork', random_day=0, random_hour=30)

    no_overlapping_day_classwork = [classwork1, classwork2, classwork3]

    temp = Student(id=1)
    temp.timetable = sub

    assert temp.calculate_day_overlapping(no_overlapping_day_classwork) == 0

def test_calculate_day_overlapping_with_overlapping():
    classwork1 = Classwork('First_classwork', random_day=0, random_hour=5)
    classwork2 = Classwork('First_classwork', random_day=0, random_hour=7)
    classwork3 = Classwork('First_classwork', random_day=0, random_hour=20)

    overlapping_day_classwork = [classwork1, classwork2, classwork3]

    temp = Student(id=1)
    temp.timetable = sub


    assert temp.calculate_day_overlapping(overlapping_day_classwork) == 60
