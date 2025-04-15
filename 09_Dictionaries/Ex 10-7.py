# ex 10-7 world winners

from itertools import count


BASE_YEAR = 1903


def main():
  year_dict = {}
  count_dict = {}

  # open the file for reading.
  with open('./09_Dictionaries/WorldSeriesWinners.txt', 'r') as input_file:
      # read all the lines
      winners = input_file.readlines()

      # add or fill the dic with the team
      for i in range(len(winners)):
        team = winners[i].rstrip('\n')

        year = BASE_YEAR + i

        # skip 1904 and 1994
        if year == 1904:
            year += 1
        if year == 1994:
            year += 1
          
        #add the team to dic with the year as a value
        year_dict[str(year)] = team
        
        # update counter
        if team in count_dict:
            count_dict[team] += 1
        else:
            count_dict[team] = 1
        # promt use to input
        
        year = input('Enter a year between 1904..')
        
        winner = year_dict[year]
        wins = count_dict[winner]
        print (f' team {year} and {winner}')
        print(f'won {wins} times')
        
    
main()
