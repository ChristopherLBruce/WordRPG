import uuid



class Item():
    """ Base class for items in game
    
    Attributes:
        name {str} -- Name of this item (default: {'ITEM'})
        description {str} -- Short description of this item (default: {'THIS IS AN ITEM'})
        weight {float} -- Weight of this item in pounds. (default: {1.0})
        value {int} -- Value of this item (default: {10})
        slot {[type]} -- Type of slote required to equip this item (default: {None})
        reqs {dict} -- Requirements to equip/use this item (default: {{'level':0,'class':None}})
    """

    def __init__(self,
                 name='ITEM',
                 description='THIS IS AN ITEM',
                 reqs=None,
                 slot=None,
                 weight=1.0,
                 value=10
                 ):
        self.name = name
        self.description = description
        self.reqs = reqs
        self.slot = slot
        self.weight = weight
        self.value = value
        self.id = self.gen_id()
        

    def gen_id(self):
        _id = uuid.uuid4()
        return _id


    def use(self):
        # check requirements before using
        pass


    def __repr__(self):
        """ Leverages the __str__ method to describe the State. """
        attrs = ','.join([f'{k}={v}' for k, v in self.__dict__.items()])
        string = f'{self.__class__.__name__}({attrs})\n'
        return string


    def __str__(self):
        """ Returns the name of the State. """
        string = f'{self.__class__.__name__}\n'
        for k, v in self.__dict__.items():
            string += f'{k} : {v}\n'
        return string


class Weapon(Item):
    """ Base class for weapons. Inherits from 'Item'
    
    Attributes:
        damage {int} -- Amount of damage this weapon does. (default: {10})
        damage_type {str} -- Type of damage this weapon does. (default: {'smashing'})
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, damage=10, damage_type='smashing',
                 name='WEAPON', description='THIS IS A WEAPON',
                 weight=1.0, value=10, slot='hand',
                 reqs={'level':0,'class':None}):
        super().__init__(name=name, description=description,
                         weight=weight, value=value, slot=slot,
                         reqs=reqs)
        self.damage = damage
        self.damage_type = damage_type


    def equip(self):
        # check requirements before equipping
        pass


    def unequip(self):
        # check conditions before unequipping
        pass


    def use(self):
        # check requirements before using
        return self.damage, self.damage_type



class Consumable(Item):
    """ Base class for weapons. Inherits from 'Item'
    
    Arguments:
        amount {int} -- [description] (default: {10})
        affects {str} -- [description] (default: {'health'})
        uses {int} -- [description] (default: {3})
    
    Returns:
        [type] -- [description]
    """

    def __init__(self, amount=10, affects='health', uses=3,
                 name='POTION', description='THIS IS A POTION',
                 weight=1.0, value=10, slot=None,
                 reqs={'level':0,'class':None}):
        super().__init__(name=name, description=description,
                         weight=weight, value=value, slot=slot,
                         reqs=reqs)
        self.amount = amount
        self.affects = affects
        self.uses = uses


    def use(self):
        # check requirements before using
        return self.amount, self.affects


"""club = Weapon(name='CLUB', description='A HEFTY WOODEN CLUB')
sword = Weapon(name='IRON SWORD', description='A SIMPLE, BUT STURDY IRON SWORD',
               reqs={'level':1, 'class':'warrior'})
staff = Weapon(name='WOOD STAFF', description='A LONG WOODEN STAFF',
               reqs={'level':1, 'class':'mage'})
health_potion = Consumable('SMALL HEALING POTION',
                        description='SMALL VIAL OF LAVENDER FLUID')

print( club )
print( sword )
print( staff )
print( health_potion )"""
