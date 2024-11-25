# Programming Exercise 9-7
# Global constant for the base year

"""
7. World Series Winners
In this chapter’s source code folder (available on the Premium Companion Website at www.
pearsonglobaleditions.com/gaddis), you will find a text file named WorldSeriesWinners.
txt. This file contains a chronological list of the World Series’ winning teams from 1903
through 2009. The first line in the file is the name of the team that won in 1903, and the
last line is the name of the team that won in 2009. (Note the World Series was not played
in 1904 or 1994. There are entries in the file indicating this.)
Write a program that reads this file and creates a dictionary in which the keys are the names
of the teams, and each key’s associated value is the number of times the team has won the
World Series. The program should also create a dictionary in which the keys are the years,
and each key’s associated value is the name of the team that won that year.
The program should prompt the user for a year in the range of 1903 through 2009. It
should then display the name of the team that won the World Series that year, and the
number of times that team has won the World Series.
    """
BASE_YEAR = 1903

def main():
    # Local dictionary variables
    year_dict = {}
    count_dict = {}
    
    # Open the file for reading
    with open('WorldSeriesWinners.txt', 'r') as input_file:
        # Read all the lines in the file into a list
        winners = input_file.readlines()

    # Fill the dictionaries with the team information.
    for i in range(len(winners)):
        team = winners[i].rstrip('\n')

        # Figure out in which year the team won 
        # (take into account skipped years)
        year = BASE_YEAR + i
        if year >= 1904:
            year += 1
        if year >= 1994:
            year += 1

        # Add information to year dictionary
        year_dict[str(year)] = team

        # Update counting dictionary
        if team in count_dict:
            count_dict[team] += 1
        else:
            count_dict[team] = 1

    # Receive user input
    year = input('Enter a year in the range 1903-2009: ')

    # Print results
    if year == '1904' or year == '1994':
        print(f"The world series wasn't played in the year {year}.")
    elif year < '1903' or year > '2009':
        print(f'The data for the year {year} is not included in our database.')
    else:
        winner = year_dict[year]
        wins = count_dict[winner]
        print(f'The team that won the world series in '
              f'{year} is the {winner}.')
        print(f'They won the world series {wins} times.')

# Call the main function.
if __name__ == '__main__':
    main()