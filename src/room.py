'''
Creates a room object that has a name and a description
'''


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    '''
    if an item is being removed from the room's list, 
    it means it's being added to the players inventory.
    So we have to return the item that was removed.
    '''
    def _remove_item(self, item_index):
        removed_item = self.items[item_index]
        self.items.pop(item_index)
        return removed_item

    def _add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return 'The room is called: {self.name}.\n{self.description}'.format(self=self)

    def __repr__(self):
        return 'Room({self.name}, {self.description})'.format(self=self)
