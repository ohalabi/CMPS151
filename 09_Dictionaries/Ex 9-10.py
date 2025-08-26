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
    outputfile = open('index.txt', 'w')

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
    with open('Kennedy.txt', 'r') as inputfile:
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