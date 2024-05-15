from abc import ABC
from abc import abstractmethod

from person import Student

class CourseAB(ABC):

    def __init__(self, name: str):
        super().__init__(self)
        self.name = name

    @abstractmethod
    def register_student(self, student: Student):
        pass

