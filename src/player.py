
'''
Creates a player object that contains a name, and what the current room location is.
'''


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def _print_current_location(self):
        print(
            f'\n{self.name}, you are currently in {self.current_room.name}.\n{self.current_room.description}')

    def _print_options(self):
        print(
            f'\nThese are your current options:\nmove with [n] [s] [e] [w]\nshow your inventory [i]\nlook for items [look around]\ngrab or drop items [grab/drop] [item name]\nquit the game: [q]\nget these options again [o]\n')

    def _move(self, direction_input):
        # attempt to move to the room there.
        try:
            self.current_room = self.current_room.__getattribute__(
                f'{direction_input}_to')
        # Print an error message if the movement isn't allowed.
        except:
            print(
                '\nThere is no way to go in that direction.\nPlease choose another option.\n')

    def _take(self, wanted_item):
        try:
            # searches through current room's index
            for index, item in enumerate(self.current_room.items):
                # if it the wanted item matches a name in the list
                if wanted_item == item.name:
                    # we save the item that is successfully
                    # removed from the current room's list
                    new_item = self.current_room._remove_item(index)
                    # add it to our inventory
                    self.inventory.append(new_item)
                    # give the user a success message
                    print(f'You picked up a {item.name}, {item.description}.')
        except:
            print(f'{item.name} is not avaliable to pick up.')

    def _drop(self, item_to_drop):
        try:
            for index, item in enumerate(self.inventory):
                if item_to_drop == item.name:
                    dropped_item = self.inventory.pop(index)
                    self.current_room._add_item(dropped_item)
                    print(f'You dropped a {item.name}.')
        except:
            print(f'{item} is not avaliable to drop.')

    def _show_inventory(self):
        if len(self.inventory) > 0:
            print('Here is what you are carrying: \n')
            for item in self.inventory:
                print(item)
            print('.')
        else:
            print('Your pockets are empty.')

    def _look_for_items(self):
        if len(self.current_room.items) > 0:
            print(f'Here is what is in {self.current_room.name}: \n')
            for item in self.current_room.items:
                print(item)
            print('.')
        else:
            print("8There's nothing in this room.")

    def __str__(self):
        return f'Your name is: {self.name}\nThe current room you are in: {self.current_room}'

    def __repr__(self):
        return f'Player({self.name}, {self.current_room})'
