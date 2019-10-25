from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
import uuid


class Room(models.Model):
    title = models.CharField(max_length=50, default="DEFAULT TITLE")
    description = models.CharField(
        max_length=500, default="DEFAULT DESCRIPTION")
    room_number = models.IntegerField(default=0, unique=True)
    treasure = models.IntegerField(default=0)
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)

    def addName(self, room_name):
        self.title = room_name
        self.save()
        return

    def setDescription(self, room_describe):
        doors = []
        if self.n_to != 0:
            doors.append("north")
        if self.s_to != 0:
            doors.append("south")
        if self.e_to != 0:
            doors.append("east")
        if self.w_to != 0:
            doors.append("west")

        if len(doors) == 1:
            add_describe = f" There is a door leading to the {doors[0]}"
        elif len(doors) > 1:
            add_describe = f" There are doors leading "
            for door in doors[:-1]:
                add_describe = str(add_describe + door + ", ")
            add_describe = str(add_describe + 'and ' + doors[-1] + '.')
        else:
            add_describe = "You are stuck, there are no exits to this room"

        self.description = room_describe + "\n" + add_describe
        self.save()

    def connectRooms(self, destinationRoom, direction):
        destinationRoomID = destinationRoom.room_number
        try:
            destinationRoom = Room.objects.get(room_number=destinationRoomID)
        except Room.DoesNotExist:
            print("That room does not exist")
        else:
            if direction == "n":
                self.n_to = destinationRoomID
            elif direction == "s":
                self.s_to = destinationRoomID
            elif direction == "e":
                self.e_to = destinationRoomID
            elif direction == "w":
                self.w_to = destinationRoomID
            else:
                print("Invalid direction")
                return
            self.save()

    def playerNames(self, currentPlayerID):
        return [p.user.username for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    def playerUUIDs(self, currentPlayerID):
        return [p.uuid for p in Player.objects.filter(currentRoom=self.id) if p.id != int(currentPlayerID)]

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            "title":       self.title,
            "description": self.description,
            "n_to":        self.n_to,
            "s_to":        self.s_to,
            "e_to":        self.e_to,
            "w_to":        self.w_to,
            "id":          self.id,
            "room_number": self.room_number,
            "treasure":    self.treasure
        }


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currentRoom = models.IntegerField(default=0)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    def initialize(self):
        if self.currentRoom == 0:
            self.currentRoom = Room.objects.first().id
            self.save()

    def room(self):
        try:
            return Room.objects.get(id=self.currentRoom)
        except Room.DoesNotExist:
            self.initialize()
            return self.room()


@receiver(post_save, sender=User)
def create_user_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_player(sender, instance, **kwargs):
    instance.player.save()
