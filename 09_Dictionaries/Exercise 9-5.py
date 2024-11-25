"""
5. Random Number Frequencies
Write a program that generates 100 random numbers between 1 and 10. The program
should store the frequency of each number generated in a dictionary with the number as
the key and the amount of times it has occurred as the value. For example, if the program
generates the number 6 a total of 11 times, the dictionary will contain a key of 6 with an
associated value of 11. Once all of the numbers have been generated, display information
about the frequency of each number.
    """

import random

# The main function.
def main():

    # Initialize an empty dictionary.
    number_dict = dict()

    # Repeat 100 times.
    for i in range(100):
        # Generate a random number between 1 and 10.
        random_number = random.randint(1, 10)

        # Establish or increment the number in the dictionary.
        if random_number not in number_dict:
            number_dict[random_number] = 1            
        else:
            number_dict[random_number] += 1

    # Display the results.
    print('Number\tFrequency')
    print('------  ---------')

    # The "sorted" function produces a sorted version of
    # the list of key-value pairs from the "items" method.
    for number, frequency in (number_dict.items()):
        print(number, frequency, sep='\t')
         

# Call the main function.
main()
