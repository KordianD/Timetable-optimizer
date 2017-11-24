import pytest
from src.Student import Student
from src.Subject import Subject
from src.Classwork import Classwork

sub = Subject('First')

@pytest.fixture
def classworks_with_overlapping():
    classworks = [Classwork('Test', random_day=0, random_hour=hour) for hour in [5, 7, 20]]
    return classworks


@pytest.fixture
def classworks_without_overlapping():
    classworks = [Classwork('Test', random_day=0, random_hour=hour) for hour in [5, 15, 30]]
    return classworks

@pytest.fixture
def multiple_classworks_with_overlapping():
    classworks = [Classwork('Test', random_day=day, random_hour=hour) for day in range(5) for hour in [5, 7, 20]]
    return classworks


def test_calculate_day_overlapping_with_no_overlapping(classworks_without_overlapping):
    no_overlapping_day_classwork = classworks_without_overlapping

    temp = Student(id=1)

    assert temp.calculate_day_overlapping(no_overlapping_day_classwork) == 0


def test_calculate_day_overlapping_with_overlapping(classworks_with_overlapping):
    overlapping_day_classwork = classworks_with_overlapping

    temp = Student(id=1)

    assert temp.calculate_day_overlapping(overlapping_day_classwork) == 60


def test_calculate_student_fitness_with_overlapping(classworks_with_overlapping):
    temp = Student(id=1)
    temp.timetable = classworks_with_overlapping

    assert temp.calculate_student_fitness() == 60


def test_calculate_student_fitness_with_multiple_overlapping(multiple_classworks_with_overlapping):
    temp = Student(id=1)
    temp.timetable = multiple_classworks_with_overlapping

    assert temp.calculate_student_fitness() == 300





