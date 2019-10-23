from django.contrib.auth.models import User
from adventure.models import Player, Room
import csv
from random import randint
​
Room.objects.all().delete()
​
map_arr = []
with open('map.csv') as map_f:
    map_r = csv.reader(map_f, delimiter=',')
    map_r.next()
    for line in map_r:
        map_arr.append(line)
​
rooms_store = {rnum: 0 for rnum in list(range(1, len(map_arr) + 1))}
treasure_room = randint(3, len(map_arr))
​
for room in rooms_store:
    rooms_store[room] = Room(title=f"room_{room}", id=room)
    if room == treasure_room:
        rooms_store[room].has_treasure = 1
    rooms_store[room].save()
​
for cons in map_arr:
​
    directions = ['n', 's', 'e', 'w']
​
    for cur_dir, con_dir in zip(directions, cons[1:5]):
        if con_dir is not None:
            rooms_store[cons[0]].connectRooms(rooms_store[con_dir], cur_dir)
​
​
​
players = Player.objects.all()
for p in players:
    p.currentRoom = rooms_store[1].id
    p.save