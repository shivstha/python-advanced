class Student:
    def __init__(self) -> None:
        self._rollno = None
        self._name = None

    def __str__(self) -> str:
        return f'{self._rollno} -> {self._name}'

    @property
    def student(self):
        print("Getting student info")
        return f'{self._rollno} -> {self._name}'

    @student.setter
    def student(self, info):
        print('Setting student info')
        self._rollno , self._name = info

s = Student()
s.student = 1, "Rama"
print(s.student)