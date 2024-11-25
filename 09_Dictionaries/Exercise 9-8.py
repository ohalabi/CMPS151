"""
    8. Pickled Vegetables
Write a program that keeps vegetable names and prices in a dictionary as key-value pairs.
The program should display a menu that lets the user see a list of all vegetables and their
prices, add a new vegetable and price, change the price of an existing vegetable, and delete
an existing vegetable and price. The program should pickle the dictionary and save it to a
file when the user exits the program. Each time the program starts, it should retrieve the
dictionary from the file and unpickle it.
    """

import pickle

# Global constants for menu choices.
DISPLAY = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for filename.
FILENAME = 'vegetables.dat'

# The main function.


def main():
    # Get vegetable data dictionary.
    data = load_data()

    # Initialize variable for user choice.
    choice = 0

    # Process user requests until user quits.
    while choice != QUIT:

        choice = get_user_choice()

        if choice == DISPLAY:
            display(data)
        elif choice == ADD:
            add(data)
        elif choice == CHANGE:
            change(data)
        elif choice == DELETE:
            delete(data)

    # Pickle the resulting dictionary.
    save_data(data)

    print('Information saved.')


def load_data():
    try:
        # Open the file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        veg_dict = pickle.load(input_file)

        # Close the file.
        input_file.close()

    # Could not open file.
    except IOError:
        # Create empty dictionary.
        veg_dict = {}

    # Return the dictionary.
    return veg_dict


def get_user_choice():
    # Display menu, get user choice, and validate it.
    print()
    print('Menu')
    print('----------------------------------------')
    print('1. Display current vegetables and prices')
    print('2. Add a vegetable and price')
    print('3. Change the price of an existing vegetable')
    print('4. Delete a vegetable and price')
    print('5. Quit the program')
    print()

    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < DISPLAY or choice > QUIT:
        choice = int(input('The choice you entered is invalid. '
                           'Please enter a valid choice: '))

    # Return user's choice.
    return choice


def display(data):
    # Check if data is empty.
    if not data:
        print('No data currently saved.')
    else:
        # Display the current data.
        print('Current vegetables and prices:')
        for veg, price in data.items():
            print(' - ', veg, ' ($', format(price, '.2f'),
                  ')', sep='')


def add(data):
    # Get vegetable name and price.
    name = input('Enter vegetable name: ')
    price = float(input('Enter price: '))

    # Add new vegetable if name does not exist.
    # Otherwise, notify user that name exists.
    if name not in data:
        data[name] = price
        print('New vegetable and price added.')
    else:
        print('That vegetable already exists.')


def change(data):
    # Get vegetable name to update price.
    name = input('Enter vegetable name: ')

    # Change price if vegetable name exists.
    # Otherwise, notify user that name does not exist.
    if name in data:
        price = float(input('Enter price: '))
        data[name] = price
        print('Vegetable price updated.')
    else:
        print('The specified vegetable was not found.')


def delete(data):
    # Get vegetable name to delete.
    name = input('Enter vegetable name: ')

    # Delete vegetable and price if name exists.
    # Otherwise, notify user that name does not exist.
    if name in data:
        del data[name]
        print('Vegetable and price deleted.')
    else:
        print('The specified vegetable was not found.')


# Function pickles the specified dictionary
# and saves it to the vegetables file.
def save_data(data):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(data, output_file)

    # Close the file.
    output_file.close()


# Call the main function.
main()
