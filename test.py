from main import StudentsInMLOps

def test_enrollStudents():
    MlopsClass = StudentsInMLOps()
    MlopsClass.enrollStudents(5)
    assert MlopsClass.getTotalStrength() == 5

def test_dropStudents():
    MlopsClass = StudentsInMLOps()
    MlopsClass.enrollStudents(10)
    MlopsClass.dropStudents(3)
    assert MlopsClass.getTotalStrength() == 7
