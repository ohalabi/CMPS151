# Named constants
STARTING_YEAR = 1993
ENDING_YEAR = 2013

# The get_price function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the Price component
# as a float.
def get_price(str):
    # Split the string at the colon.
    items = str.split(':')
    # Return the price, as a float.
    return float(items[1])

# The get_month function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the MM component
# as an int.
def get_month(str):
    # Split the string at the hyphens.
    items = str.split('-')
    # Return the month, as an int.
    return int(items[0])

# The get_day function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the DD component
# as an int.
def get_day(str):
    # Split the string at the hyphens.
    items = str.split('-')
    # Return the day, as an int.
    return int(items[1])

# The get_year function accepts a string that is assumed to be
# in the format MM-DD-YYYY:Price. It returns the YYYY component
# as an int.
def get_year(str):
    # Split the string at the colon.
    items = str.split(':')
    # Split the date item at the hyphens.
    date_items = items[0].split('-')
    # Return the year, as an int.
    return int(date_items[2])

# The get_yearly_average function has two parameters: gas_list and year.
# The gas_list parameter is a list of strings, where each string is assumed
# to be in the format MM-DD-YYYY:Price. The year parameter is a numeric
# value assumed to be a year. The function returns the average price for
# for all elements where the YYYY component is equal to the year parameter.
def get_yearly_average(gas_list, year):
    # Initialize an accumulator.
    total = 0

    # Initialize a counter.
    count = 0

    # Step through the list, getting the sum of all the prices
    # for the specified year.
    for e in gas_list:
        if get_year(e) == year:
            total += get_price(e)
            count += 1

    # Calculate the average.
    average = total / count

    # Return the average.
    return average

def main():
    # Open the file.
    with open('GasPrices.txt', 'r') as gas_file:
        # Read the file's contents into a list.
        gas_list = gas_file.readlines()

        # Display the average price for each year.
        for i in range(STARTING_YEAR, ENDING_YEAR + 1):
            print(f'The average price in {i} was $'
                f'{get_yearly_average(gas_list, i):.2f}')
    
# Call the main function.
if __name__ == '__main__':
    main()