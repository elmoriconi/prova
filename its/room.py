class Room:

    def __init__(self, name: str, floor: int, num_seats: int):
        self.name: str = name
        self.floor: int = floor
        self.num_seats: int = num_seats

    def set_name(self, name: str):
        self.name = name

    def set_floor(self, floor: int):
        self.floor = floor

    def set_num_seat(self, num: int):
        self.num_seats = num

    def get_name(self) -> str:
        return self.name

    def get_floor(self) -> int:
        return self.floor
    
    def get_num_seats(self) -> int:
        return self.num_seats
    