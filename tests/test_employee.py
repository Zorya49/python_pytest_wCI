import pytest
from resources import Employee


@pytest.fixture()
def employee():
    return Employee("John Doe", 5, positions=["Junior Python Developer", "Software Test Engineer"])


def test_init(employee: Employee):
    assert employee.name == "John Doe"
    assert employee.experience == 5
    assert employee.positions == ["Junior Python Developer", "Software Test Engineer"]


def test_forename(employee: Employee):
    assert employee.forename == "John"


def test_surname(employee: Employee):
    assert employee.surname == "Doe"


def test_no_surname(employee: Employee):
    employee.name = "John"
    assert not employee.surname


def test_no_positions():
    employee = Employee("Johnny Doe", 0)
    assert employee.positions == []


def test_add_experience(employee: Employee):
    employee.add_experience()
    assert employee.experience == 6


def test_add_position(employee: Employee):
    employee.add_position("CySe Engineer")
    assert employee.positions == ["Junior Python Developer", "Software Test Engineer", "CySe Engineer"]
