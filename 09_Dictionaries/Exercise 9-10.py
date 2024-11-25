
"""
10. Word Index

Write a program that reads the contents of a text file. The program should create a dictionary
in which the key-value pairs are described as follows:
- Key. The keys are the individual words found in the file.
- Values. Each value is a list that contains the line numbers in the file where the word
(the key) is found.

For example, suppose the word “robot” is found in lines 7, 18, 94, and 138. The dictionary
would contain an element in which the key was the string “robot”, and the value was a list
containing the numbers 7, 18, 94, and 138.

Once the dictionary is built, the program should create another text file, known as a word
index, listing the contents of the dictionary. The word index file should contain an alphabetical
listing of the words that are stored as keys in the dictionary, along with the line
numbers where the words appear in the original file. Figure 9-1 shows an example of an
original text file (Kennedy.txt) and its index file (index.txt).
"""

# 
# The get_word_dict function returns a dictionary containing
# the words from line_list as keys, and their line numbers
# as values.
def get_word_dict(line_list):
    # Create a line counter.
    count = 0
    
    # Create a dictionary to hold the words.
    word_dict = {}

    # Step through the list of lines.
    for e in line_list:
        # Split the line into words.
        words = e.split(' ')

        # Step through the list of words.
        for w in words:
            # If the word is in the dictionary...
            if w in word_dict:
                # Update the existing element.
                word_dict[w].add(count + 1)
            else:
                # Otherwise, store the word in the dictionary.
                word_dict[w] = set([count + 1])

        # Update the counter.
        count += 1

    # Return the dictionary.
    return word_dict

# The write_index_file function writes an index file containing the
# elements of the word_dict dictionary.
def write_index_file(word_dict):
    # Open the file.
    outputfile = open('./09_Dictionaries/index.txt', 'w')

    # Write the entries from the dictionary.
    for key in word_dict:
        # Write the word.
        outputfile.write(key + ': ')
        # Write the line numbers.
        for val in word_dict[key]:
            outputfile.write(str(val) + ' ')
        # Write a newline character.
        outputfile.write('\n')

    # Close the file.
    outputfile.close()
    
def main():
    # Open the file.
    with open('./09_Dictionaries/Kennedy.txt', 'r') as inputfile:
        # Read the file's contents into a list.
        line_list = inputfile.readlines()

    # Strip the newline from each list element.
    for i in range(len(line_list)):
        line_list[i] = line_list[i].rstrip('\n')

    # Get a dictionary holding the words and their line numbers.
    word_dict = get_word_dict(line_list)

    # Write the index file.
    write_index_file(word_dict)
    
# Call the main function.
if __name__ == '__main__':
    main()