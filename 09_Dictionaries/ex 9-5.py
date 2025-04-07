#eEx 9-5 random Number freq
import random

def main():
    number_dict = dict()
    
    for i in range(100):
        random_number = random.randint(1, 10)
        
        if random_number not in number_dict:
            number_dict[random_number] = 1
        else:
            number_dict[random_number] += 1
    
    print('Number\tFrequency')
    print('_____\t________')
    for number, frquency in sorted(number_dict.items()):
        print(number, frquency, sep='\t')
main()