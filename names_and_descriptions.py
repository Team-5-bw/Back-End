from random import choice
from typing import List, Any, Union

from adventure.models import Room


class ndGenerator:

    types = {1: 'stable',
             2: 'wine cellar',
             3: 'workshop',
             4: 'empty kennel',
             5: 'room full of rubble',
             6: 'catacombs',
             7: 'storage room',
             8: 'empty room',
             9: 'natural cavern',
             10: 'weapons locker',
             11: 'well room',
             12: 'sculpture room',
             13: 'bridge room'}

    adj_atmos = ['clean', 'dank', 'musty', 'dimly lit', ' bright', 'dusty', 'old', 'new looking']
    adj_phys = ['high ceilinged', 'low', 'drafty', 'graffitied', 'still', 'breezy', 'arch vaulted']

    contents = dict({"stable": [" with harnesses and saddles hanging on the walls.",
                           " full of broken stalls, but otherwise lacking equine paraphernalia.",
                           " with a smelly pile of horse dung pushed into the corner",
                           "An empty paint can sits on a shelf. The room is otherwise empty."],
                "wine cellar": [str(". Massive wine barrels are stacked against the walls, " +
                                    "along with a few broken barrels in the middle of the room"),
                                str("Vintage wine bottles line the walls in racks. A number of empty bottles " +
                                    "litter the floor, along with a dirty shirt, spilled tobacco, and a broken pipe"),
                                " the floor is covered in broken bottles. Thankfully you are wearing heavy boots",
                                str(" a man is passed out in the corner with obscene pictures drawn on his face. " +
                                    "He is lies in a puddle of spilled wine surrounded by empty bottles. You are " +
                                    "unable to wake him")],
                "workshop": [" tools hang on the walls, and an unidentifiable object sets on a bench.",
                             str(" a wooden boat is propped up in the center of the room. Part of it's side appears t" +
                                 "o have been smashed with a hammer. Neither the hammer nor the hammerer are present."),
                             str(" an empty workbench sets against one wall, and a large, menacing machine hulks in " +
                                 "one corner. The room is otherwise empty"),
                             ", rusty bicycle parts litter the floor, and a bent frame sets on a work bench."],
                "empty kennel": [". Several dog houses line one wall. There are empty bags of dog treats on the floor",
                                 ". No doggos are in sight",
                                 str(". Suddenly, a very small dog that looks like a rug runs out of a tiny dog door " +
                                     "and barks ferociously. He poses you no threat, but you decide to leave. The " +
                                     "pup feels satisfaction in a job well done"),
                                 str(". A very small cat sleeps on top of the lone dog house, and a dead rat is " +
                                     "placed in front of the door you just entered. The cat looks so peaceful you "+
                                     "decide to leave it be.")],
                "room full of rubble": [". You climb carefully through"],
                "catacombs": [", stone markers line the walls. The dead seem quiet.",
                              str(" someone has removed bones from one of the crypts and made a small sculpture on" +
                                  " the floor. Burned out candles sit in a circle."),
                              str(". A wizened ghostly face materializes in the wall and begins shouting at you to " +
                                  "'get off my lawn' and finally leaves muttering about 'kids these days'")],
                "storage room": [" full of greek amphorae.", ", pallets are stacked haphazardly about.",
                                 " full of strange shaped objects wrapped in plastic.",
                                 str(". Boxes are stacked randomly. They contain toiletries, a few action figures," +
                                     " an out of tune guitar, and various posters, mostly promoting bands you don't" +
                                     " recognize"),
                                 ", the floor is strewn with packing peanuts and empty amazon boxes",
                                 ", empty except for a pile of crushed aluminum cans in the corner",
                                 str(", a table sets in the center, upon which is a large bowl of liquid mercury. " +
                                     "An origami boat floats on the surface"),
                                 ", piled high with discarded tires. The room reeks of rubber",
                                 str(", you find three large bins labeled recycling for plastic, cardboard, and glass. Each is filled with a mixture of household trash"),
                                 ", there is nothing stored here"],
                "empty room": [". It is empty."],

                "natural cavern": [". Stalactites hang from the ceiling and one wall is covered in flowstone.",
                                   ". Crystals sparkle on the walls. A small bat flies overhead",
                                   ". You find a white snake without eyes. It slithers into a crack."],

                "weapons locker": [". The weapons are gone", ". Several locked gun safes line the walls. You find a hammer",
                                   ". You discover a crate of military issue swords. They are all rusted beyond usability."],

                "well room": [". In the center of the room is a deep well", ". This room makes you feel well",
                              ". This room looks well used"],

                "sculpture room": [" full of marble busts", ". The sculptures are gone. Pedestals remain.",
                                   str(". In the center of the room is a large stone statue of a human like creature" +
                                       " with tentacles and wings. It unsettles you.")],

                "bridge room": [str(" thin stone bridges connect the doors to the center of the room. Below is a " +
                                    "yawning chasm. You cross carefully. Fortunately there are no Balrogs here")]
                })

    def __init__(self, room):
        self.room = room
        room_number = self.room.room_number
        if room_number > 40:
            self.name_n = choice(list(range(1, 6)) + [7, 8, 10])
        else:
            self.name_n = choice(list(range(5, 14)))
        name_string = self.types[self.name_n]
        self.room_name = str("A " + choice(self.adj_atmos) + " " + choice(self.adj_phys) + " " + self.types[self.name_n])

        self.description = choice(self.contents[name_string])

    def get_name(self):
        return self.room_name

    def get_desc(self):
        return self.description

    def get_combined(self):
        return str(self.room_name + self.description)
