from . import Slot
from ..inventory import Inventory


# default slots for humanoid character or the player
DEF_SLOTS = (
    Slot('head'),
    Slot('hand_left', _type='hand'),
    Slot('hand_right', _type='hand'),
    Slot('chest'),
    Slot('legs'),
    Slot('feet')
    )


class Actor:
    """ Most base class for any entity in the game
    
    Attributes:
        name {str} -- Name of this entity
        race {str} -- Race or species of this entity. Used to determine base
                      stats, abilities, etc.
    """
    def __init__(self, name, race, inventory):
        self.name = name
        self.race = race
        self.inventory = inventory



class Character(Actor):
    """ Class for entities that have basic ability to enter combat
    
    Inherits from Actor

    Attributes:
        name {str} -- Name of this entity
        race {str} -- Race or species of this entity. Used to determine base
                      stats, abilities, etc.
        role {str} -- Class of this character
        level {int} -- Level of this character
        slots {list} -- List of 'Slot' objects

    """

    def __init__(self, name, race, inventory, role, level=1, slots=DEF_SLOTS):
        super().__init__(name, race, inventory)
        self.role = role
        self.slots = slots       
        self.level = self.set_level(level)
        self.health_max = self.set_health_max()
        self.health_cur = self.health_max


    def set_level(self, level):
        return level


    def set_health_max(self):
        # use race, class, level formula to determine base hit points
        return health_max


    def change_health(self, amount):
        self.health_cur += amount





class Player(Character):
    """ Class for player character.
    
    name, race, inventory, role, level=1, slots

    Inherits from Character
    """
    def __init__(self, name, race, inventory, role, level=1, slots=DEF_SLOTS):
        super().__init__(self, name, race, inventory, role, level, slots )
        self.experience = self.set_experience()

        # not sure if we want to store position here.  Right now the Game_Map
        # class handles position in the various maps
        # self.pos_x = 0
        # self.pos_y = 0


    def set_experience(self):
        # get experience based on LEVEL_XP table
        experience = 0
        return experience


    def change_experience(self, amount):
        # change experience and check to see if character can level up
        pass


    def equip(self, item):
        """ Equips an item

        Calls .equip() method on appropriate Slot
        
        Arguments:
            item {[type]} -- [description]
        """
        pass


    def unequip(self, item):
        """ Unequips an item

        Calls .equip() method on appropriate Slot
        
        Arguments:
            item {[type]} -- [description]
        """
        pass


    # These should be handled through equipped items
    # def melee_attack(self):
    #     return 17

    # These should be handled through equipped items
    # def magic_attack(self):
    #     pass

    # def health_generation(self):
    #     pass

    # This is all handled in game state
    # def move(self, _dir):
    #     directions = {"North": (0, -1), "South": (0, 1), "East": (1, 0), "West": (-1, 0)}
    #     delta_x, delta_y = directions[_dir]
    #     new_x, new_y = self.pos_x + delta_x, self.pos_y + delta_y
    #     if WorldMap.access_information(new_x, new_y, "Crossable"):
    #         self.pos_x, self.pos_y = new_x, new_y
    #     else:
    #         clear()
    #         print("You cannot cross here:")
    #         print(WorldMap.access_information(new_x, new_y, "Name"))
    #         pause()



    # # TODO methods like this should probably be moved to mechanics
    # # the script classes shouldn't be dealing with UI, only handling the class instances
    # def inspect_area(self):
    #     info = {
    #         "Name": WorldMap.access_information(self.pos_x, self.pos_y, "Name"),
    #         "Resources": WorldMap.access_information(self.pos_x, self.pos_y, "Resources"),
    #         "Spawns": WorldMap.access_information(self.pos_x, self.pos_x, "Spawns"),
    #         "Info": WorldMap.access_information(self.pos_x, self.pos_y, "Info")
    #     }
    #     clear()
    #     print("Name: " + str(info["Name"]))
    #     print("Resources: " + str(info["Resources"]))
    #     print("Spawns: " + str(info["Spawns"]))
    #     print("Info: " + str(info["Info"]))
    #     pause()


# This class is probably redundant with base 'Character' class.
# class Enemy(Character):
#     """ Enemies
    
#     Inherits:
#         Character {[type]} -- [description]
    
#     Returns:
#         [type] -- [description]
#     """

    
#            # Combat based entities
#     def __init__(self, name, level, health_points):
#         super().__init__(name, level)
#         self.hp = health_points

#     # def melee_attack(self):
#     #     return 5