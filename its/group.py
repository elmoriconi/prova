from group import Student

class Group:

    def __init__(self, name: str, limit_students: int):
        self.name: str = name
        self.limit_students: int = limit_students
        self.students: list[int] = []

    def get_name(self) -> str:
        return self.name
    
    def get_limit_students(self) -> int:
        return self.limit_students
    
    def add_student(self, student: Student):
        if student not in self.students and self.get_limit_students() > 0:
            self.students.append(student)
            self.limit_students -= 1
            return True
        return False