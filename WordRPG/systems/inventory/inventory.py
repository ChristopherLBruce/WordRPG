

class Inventory():
    def __init__(self, items=[], limit=10):
        self.inventory = items
        self.limit = limit


    # Add item to inventory if space is available
    # Return true if add was successful
    def add(self, item):
        """[summary]
        
        Arguments:
            item {[type]} -- [description]
        
        Returns:
            bool -- True if item was added, False otherwise
        """
        if len(self.inventory) >= self.limit:
            return False
        else:
            self.inventory.append(item)
            return True


    def get_index(self, item):
        """ find index for item in inventory
        
        Arguments:
            item {item} -- an item object
        """
        pass


    # Remove item at given position
    def remove(self, index):
        """ Remove item at given index
        
        Arguments:
            index {int} -- Index of item to remove from inventory
        
        Raises:
            ValueError -- [description]
        
        Returns:
            bool -- True if item was removed, False otherwise
        """
        if index in range(len(self.inventory)):
            del self.inventory[index]
            return True
        else:
            raise ValueError(f'Index {index} invalid for inventory {self.inventory}')
            return False
