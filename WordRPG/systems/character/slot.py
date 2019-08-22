class Slot:
    def __init__(name, _type=None, item=None):
        self.name = name,
        
        if _type is not None:
            self.type = _type
        else:
            self.type = name

        self.item = item,
    

    def equip(self):
        pass


    def unequip(self):
        pass


    def show(self):
        pass
