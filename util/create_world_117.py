from django.contrib.auth.models import User
from adventure.models import Player, Room
import csv
from random import randint

Room.objects.all().delete()

map_arr = []
with open('map.csv') as map_f:
    map_r = csv.reader(map_f, delimiter=',')
    next(map_r)
    for line in map_r:
        map_arr.append([int(x) if x != '' else None for x in line])

rooms_store = {rnum: 0 for rnum in list(range(1, len(map_arr) + 1))}
#treasure_room = randint(3, len(map_arr))

for room in rooms_store:
    rooms_store[room] = Room(title=f"room_{room}",
                             room_number=room
                             )
#    if room == treasure_room:
#        rooms_store[room].has_treasure = 2
    rooms_store[room].save()

directions = ['n', 's', 'e', 'w']

for connect in map_arr:
    for dir, con in zip(directions, connect[1:5]):
        print(dir, con)
        if con is not None:
            rooms_store[connect[0]].connectRooms(rooms_store[con], dir)



players = Player.objects.all()
for p in players:
    p.currentRoom = rooms_store[1].id
    p.save()
