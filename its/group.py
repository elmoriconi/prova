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