
from room import Room

class Building:

    def __init__(self, name: str, address: str, floors: int):
        self.name: str = name
        self.address: str = address
        self.floors: int = floors
        self.rooms: list[Room] = []

    def add_rooms(self, room: Room):
        lower, upper = self.get_floors()
        if room not in self.get_rooms() and lower <= self.get_floors() <= upper:
            self.rooms.append(room)
            return True
        return False

    def set_name(self, name: str):
        self.name = name

    def set_floors(self, floors: int):
        self.floor = floors

    def set_address(self, address: str):
        self.address = address

    def get_name(self) -> str:
        return self.name

    def get_floors(self) -> int:
        return self.floors
    
    def get_address(self) -> int:
        return self.address
    
    def get_rooms(self) -> list[Room]:
        return self.rooms

    def __str__(self) -> str:
        s: str = f"Edificio: {self.get_name()}, indirizzo: {self.get_address()}, piani: {self.get_floors()}"
        s += ""
        for room in self.get_rooms():
            s += ""