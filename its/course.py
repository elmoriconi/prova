from building import Building
from group import Group

class Course:

    def __init__(self, name: str, building: Building):
        self.name: str = name
        self.building: Building = building
        self.groups: list[int] = []

    def get_name(self):
        return self.name
    
    def get_building(self):
        return self.building
    
    def __str__(self) -> str:
        pass