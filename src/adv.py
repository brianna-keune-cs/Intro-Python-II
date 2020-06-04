from room import Room
from player import Player
from item import Item

# Todo:
# create a way to save your game.

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare items
items = {
    'pen': Item('pen', 'a plain blue pen'),
    'treasure': Item('treasure', 'your favourite chapstick'),
    'notebook': Item('notebook', 'just a red notebook'),
    'hat': Item('hat', 'a fancy straw hat')
}

room['outside']._add_item(items['pen'])
room['foyer']._add_item(items['notebook'])
room['overlook']._add_item(items['treasure'])
room['overlook']._add_item(items['hat'])


# avalible commands:
command = {
    'moves': ['n', 's', 'e', 'w'],
    'quit': ['q', 'quit', 'exit'],
    'options': ['o', 'help'],
    'actions': ['take', 'drop'],
    'inventory': ['i'],
    'checkitems': ['look', 'around']
}


'''Runs the game when called from main'''


def _run_game():
    running = True  # let's us know if the game is running

    # takes in user name first
    user_input = input('Greetings adventurer! What is your name?\n\n>> ')

    # Make a new player object that is currently in the 'outside' room.
    player1 = Player(user_input, room['outside'])  # todo, verify string??
    print(
        f"Welcome {player1.name}!\nOh the great outdoors.\nWhy don't you have a [look around]?\nGood luck finding the treasure!\nMove with [n] [s] [e] [w]")
    # game logic
    # Write a loop that:
    while (running is not False):
        # * Prints the current room name
        # * Prints the current description (the textwrap module might be useful here).
        player1._print_current_location()

        # * Waits for user input and decides what to do.
        user_input = input(
            '\nWhat would like to do next? [o] for options.\n\n>> ').split(' ')
        user_input_len = len(user_input)

        # user inserts single command from options
        if user_input_len is 1:
            action = user_input[0]

            if action in command['options']:
                player1._print_options()

            # If the user enters a cardinal direction, attmpet to move
            if action in command['moves']:
                player1._move(action)

            # If the user enters "q", quit the game.
            if action in command['quit']:
                running = False
                print('You have quit the game. Goodbye!')

            # if user wants to see what's in their inventory
            if action in command['inventory']:
                player1._show_inventory()

        # user enters complex command
        if user_input_len is 2:
            action, item = user_input[0], user_input[1]
            if action in command['actions']:
                if action == 'take':
                    player1._take(item)
                if action == 'drop':
                    player1._drop(item)
            if action == 'look' and item == 'around':
                player1._look_for_items()


if __name__ == "__main__":
    _run_game()
