from room import Room
from building import Building

r: Room = Room("213", 2, 30)
print(r)

b: Building = Building("SMI", "Via della Sierra Nevada 60", 5)
print(b)
print(len(b.get_rooms()))


